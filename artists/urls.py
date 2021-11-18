from django.urls import path
from . import views

urlpatterns = [
    path('<artist_id>', views.artist_bio, name='artist_bio'),
]