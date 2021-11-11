from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from .models import Print, PrintOption

# Create your views here.


def all_products(request):
    """ View to show all print products, incl sorting and search queries """

    products = Print.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(title__icontains=query) | Q(artist__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
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