from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Print, PrintOption


def bag_contents(request):
    """
    Project wide context used across the apps to keep track of the
    bag/cart and how many prints of each item/size are in the bag
    """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    # remove items from bag if they no longer exist in the db
    # this is to handle case where print is deleted while in
    # a cart
    missing_prints = []
    for item_id, item_data in bag.items():
        num_prints = Print.objects.filter(pk=item_id).count()
        if not num_prints:
            missing_prints.append(item_id)

    for key in missing_prints:
        bag.pop(key, None)

    for item_id, item_data in bag.items():
        product = get_object_or_404(Print, pk=item_id)
        for size, quantity in item_data['items_by_size'].items():
            # get the price based on the size
            option = get_object_or_404(PrintOption, size=size)
            price = option.price
            dimensions = option.dimensions
            # deduct 20% if this is a dicounted item
            if product.discount_applies:
                price = price / 5 * 4
            total += quantity * price
            product_count += quantity
            bag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
                'price': price,
                'dimensions': dimensions,
                'size': size,
            })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
