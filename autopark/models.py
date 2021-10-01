from django.db import models


# Create your models here.

class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto-park'

    brand = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand
