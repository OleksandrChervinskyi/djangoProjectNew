from django.db import models
from django.core import validators as v


# Create your models here.

class PlaneModel(models.Model):
    class Meta:
        db_table = 'planes'

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(default=1900)
    country = models.CharField(max_length=100, validators=[v.MinLengthValidator(2)])
    length = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

    def __str__(self):
        return self.brand
