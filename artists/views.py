from django.shortcuts import render, get_object_or_404
from .models import Artist


def artist_bio(request, artist_id):
    """ A view to show individual artist details """

    artist = get_object_or_404(Artist, id=artist_id)

    context = {
        'artist': artist,
    }

    return render(request, 'artists/artist_bio.html', context)