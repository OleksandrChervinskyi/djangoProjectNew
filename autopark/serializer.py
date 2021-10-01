from rest_framework import serializers as s

from autopark.models import AutoParkModel
from cars.serializer import CarsSerializers


class AutoParkSerializers(s.ModelSerializer):
    cars = CarsSerializers(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('brand', 'city', 'cars')
