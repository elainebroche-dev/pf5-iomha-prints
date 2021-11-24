from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:artist_id>/', views.artist_bio, name='artist_bio'),
    path('summernote/', include('django_summernote.urls')),
    path('add_artist/', views.add_artist, name='add_artist'),
    path('edit_artist/<int:artist_id>/', views.edit_artist, name='edit_artist'),
    path('delete_artist/<int:artist_id>/', views.delete_artist, name='delete_artist'),
]