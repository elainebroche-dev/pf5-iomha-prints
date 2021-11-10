from django.db import models
from django.contrib.auth.models import User

SIZES = ((0, "Small"), (1, "Medium"), (2, "Large"))
RATING = ((0, "Unrated"), (1, "Poor"), (2, "Fair"), (3, "Good"), (4, "Very Good"), (5, "Excellent"))


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Print(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    title = models.CharField(max_length=254)
    artist = models.CharField(max_length=254)
    rating = models.IntegerField(choices=RATING, default=0, blank=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)
    discount_applies = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='print_likes', blank=True)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class PrintOption(models.Model):
    size = models.IntegerField(choices=SIZES)
    dimensions = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)