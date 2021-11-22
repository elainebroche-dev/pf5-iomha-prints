from django.urls import path, include
from . import views

urlpatterns = [
    path('<artist_id>', views.artist_bio, name='artist_bio'),
    path('summernote/', include('django_summernote.urls')),
]