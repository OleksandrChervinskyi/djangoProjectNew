from rest_framework import serializers as s

from .models import PlaneModel


class PlaneSerializer(s.ModelSerializer):
    class Meta:
        model = PlaneModel
        fields = '__all__'
