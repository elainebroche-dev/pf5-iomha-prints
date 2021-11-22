from django.contrib import admin
from .models import Artist
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Artist)
class ArtistAdmin(SummernoteModelAdmin):
    list_display = (
        'name',
        'nationality',
        'dob',
        'image',
    )

    summernote_fields = ('bio',)

    ordering = ('name',)

