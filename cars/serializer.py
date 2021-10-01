from rest_framework import serializers as s

from cars.models import CarsModel


class CarsSerializers(s.ModelSerializer):
    class Meta:
        model = CarsModel
        fields = '__all__'
