from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Print, PrintOption, Category
from datetime import datetime, timedelta
from django.db.models.functions import Lower

# Create your views here.


def all_products(request):
    """ View to show all print products, incl sorting and search queries """

    products = Print.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'title':
                sortkey = 'lower_title'
                products = products.annotate(lower_title=Lower('title'))

            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'discount' in request.GET:
            products = products.filter(discount_applies=True)

        # new arrivals will have an added_on date within the last 6 months
        if 'newarrivals' in request.GET:
            products = products.filter(added_on__gte=datetime.now()-timedelta(days=182))

        if 'wishlist' in request.GET:
            products = products.filter(likes__id=request.user.id)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
 
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(title__icontains=query) | Q(artist__name__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual print details """

    product = get_object_or_404(Print, pk=product_id)
    options = PrintOption.objects.all().order_by('-price')

    liked = False
    if product.likes.filter(id=request.user.id).exists():
        liked = True

    context = {
        'product': product,
        'options': options,
        'liked' : liked,
    }

    return render(request, 'products/product_detail.html', context)

def like_product(request, product_id):
    """ A view to like/unlike a print """

    product = get_object_or_404(Print, pk=product_id)

    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)

    return HttpResponseRedirect(reverse('product_detail', args=[product_id]))