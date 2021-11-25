from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Define visible list of fields
    """
    list_display = (
        'default_street_address1',
        'default_street_address2',
        'default_town_or_city',
        'default_county',
        'default_postcode', 
        'default_country' 
    )

