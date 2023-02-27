from django.db import models

# Create your models here.

class Product(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.FloatField()
    release_date = models.DateField()

    