from datetime import datetime, timedelta
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Print, PrintOption, Category
from .forms import PrintForm, PrintOptionForm


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
            products = products.filter(added_on__gte=datetime.now() -
                                       timedelta(days=182))

        if 'wishlist' in request.GET:
            products = products.filter(likes__id=request.user.id)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = (Q(title__icontains=query) |
                       Q(artist__name__icontains=query))
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
        'liked': liked,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def like_product(request, product_id):
    """ A view to like/unlike a print """

    product = get_object_or_404(Print, pk=product_id)

    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
    else:
        product.likes.add(request.user)

    return HttpResponseRedirect(reverse('product_detail', args=[product_id]))


@login_required
def add_print(request):
    """ Add a print to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PrintForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added print!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add print. Please ensure the form is valid.')
    else:
        form = PrintForm()

    template = 'products/add_print.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_printoption(request, option_size):
    """ Update a print option in the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    option = get_object_or_404(PrintOption, size=option_size)

    if request.method == 'POST':
        form = PrintOptionForm(request.POST, request.FILES, instance=option)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated print option!')
            return redirect(reverse('edit_printoption', args=[option.size]))
        else:
            messages.error(
                request,
                'Failed to update print option. '
                'Please ensure the form is valid.')
    else:
        form = PrintOptionForm(instance=option)
        messages.info(request, f'You are editing {option.dimensions}')

    template = 'products/edit_printoption.html'
    context = {
        'form': form,
        'option': option,
    }

    return render(request, template, context)


@login_required
def edit_print(request, product_id):
    """ Edit a print in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Print, pk=product_id)
    if request.method == 'POST':
        form = PrintForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated print!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update print. Please ensure the form is valid.')
    else:
        form = PrintForm(instance=product)
        messages.info(request, f'You are editing {product.title}')

    template = 'products/edit_print.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_print(request, product_id):
    """ Delete a print from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Print, pk=product_id)
    product.delete()
    messages.success(request, 'Print deleted!')
    return redirect(reverse('products'))
