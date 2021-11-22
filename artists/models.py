from django.db import models

class Artist(models.Model):

    name = models.CharField(max_length=254, unique=True)
    nationality = models.CharField(max_length=254)
    bio = models.TextField()
    image = models.ImageField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
