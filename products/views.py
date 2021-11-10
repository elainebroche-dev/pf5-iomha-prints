from django.shortcuts import render
from .models import Print

# Create your views here.


def all_products(request):
    """ View to show all print products, incl sorting and search queries """

    products = Print.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)