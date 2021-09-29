from django.core import validators as v
from django.db import models

# Create your models here.
from plane_park.models import PlaneParkModel


class PlaneModel(models.Model):
    class Meta:
        db_table = 'planes'

    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    country_of_manufacture = models.CharField(max_length=255)
    length = models.IntegerField(default=0, blank=True, validators=[v.MaxValueValidator(100000, 'Too much')])
    height = models.IntegerField(default=0)
    wingspan = models.IntegerField(default=0)
    load_capacity = models.IntegerField(default=0)

    plane_park = models.ForeignKey(PlaneParkModel, on_delete=models.CASCADE, related_name='planes')
