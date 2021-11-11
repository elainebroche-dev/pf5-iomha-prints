from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Print, PrintOption

# Create your views here.


def all_products(request):
    """ View to show all print products, incl sorting and search queries """

    products = Print.objects.all()

    context = {
        'products': products,
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