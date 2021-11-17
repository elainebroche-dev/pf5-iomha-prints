from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Print, PrintOption


# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified print to the shopping cart """

    product = get_object_or_404(Print, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    size = request.POST['product_size']
    option = get_object_or_404(PrintOption, size=size)
    size_name = option.dimensions.split()[0]

    bag = request.session.get('bag', {})

    
    if item_id in list(bag.keys()):
        if size in bag[item_id]['items_by_size'].keys():
            bag[item_id]['items_by_size'][size] += quantity
            messages.success(request, f'Updated size {size_name} {product.title} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Added size {size_name} {product.title} to your bag')
    else:
        bag[item_id] = {'items_by_size': {size: quantity}}
        messages.success(request, f'Added size {size_name} {product.title} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified print to the specified amount"""

    product = get_object_or_404(Print, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    size = request.POST['product_size']
    option = get_object_or_404(PrintOption, size=size)
    size_name = option.dimensions.split()[0]
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id]['items_by_size'][size] = quantity
        messages.success(request, f'Updated size {size_name} {product.title} quantity to {bag[item_id]["items_by_size"][size]}')
    else:
        del bag[item_id]['items_by_size'][size]
        if not bag[item_id]['items_by_size']:
            bag.pop(item_id)
        messages.success(request, f'Removed size {size_name} {product.title} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Print, pk=item_id)
        size = request.POST['product_size']
        option = get_object_or_404(PrintOption, size=size)
        size_name = option.dimensions.split()[0]
        bag = request.session.get('bag', {})

  
        del bag[item_id]['items_by_size'][size]
        if not bag[item_id]['items_by_size']:
            bag.pop(item_id)
        messages.success(request, f'Removed size {size_name} {product.title} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)