from django.contrib import admin
from .models import Print, Category, PrintOption


class PrintAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'artist',
        'category',
        'rating',
        'image',
        'added_on',
        'discount_applies'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class PrintOptionAdmin(admin.ModelAdmin):
    list_display = (
        'size',
        'dimensions',
        'price',
    )


admin.site.register(Print, PrintAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PrintOption, PrintOptionAdmin)
