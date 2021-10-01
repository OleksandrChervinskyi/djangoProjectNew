from django.db import models
from autopark.models import AutoParkModel
# Create your models here.


class CarsModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
