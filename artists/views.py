from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Artist
from .forms import ArtistForm


def artist_bio(request, artist_id):
    """ A view to show individual artist details """

    artist = get_object_or_404(Artist, id=artist_id)

    context = {
        'artist': artist,
    }

    return render(request, 'artists/artist_bio.html', context)


@login_required
def add_artist(request):
    """ Add an artist to the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added artist!')
            return redirect(reverse('add_artist'))
        else:
            messages.error(request, 'Failed to add artist. \
                Please ensure the form is valid.')
    else:
        form = ArtistForm()

    template = 'artists/add_artist.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_artist(request, artist_id):
    """ Edit an artist in the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=artist_id)
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES, instance=artist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated artist!')
            return redirect(reverse('artist_bio', args=[artist.id]))
        else:
            messages.error(request, 'Failed to update artist. \
                Please ensure the form is valid.')
    else:
        form = ArtistForm(instance=artist)
        messages.info(request, f'You are editing {artist.name}')

    template = 'artists/edit_artist.html'
    context = {
        'form': form,
        'artist': artist,
    }

    return render(request, template, context)


@login_required
def delete_artist(request, artist_id):
    """ Delete an artist from the database """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    artist = get_object_or_404(Artist, pk=artist_id)
    artist.delete()
    messages.success(request, 'Artist deleted!')
    return redirect(reverse('products'))
