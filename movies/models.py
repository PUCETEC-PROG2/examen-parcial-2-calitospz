from django.db import models
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=30, null=False)
    genre = models.CharField(max_length=30, null=False)
    director_name = models.CharField(max_length=30, null=False)
    publication_year = models.CharField(max_length=30, null=False)
    synopsis = models.TextField(null=False)
    
    def __str__(self):
        return self.title
# Create your models here.
