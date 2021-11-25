from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Artist


@admin.register(Artist)
class ArtistAdmin(SummernoteModelAdmin):
    """
    Define visible list of fields, WYSIWYG bio field and default ordering
    for Artist Model
    """
    list_display = (
        'name',
        'nationality',
        'dob',
        'image',
    )

    summernote_fields = ('bio',)

    ordering = ('name',)
