from rest_framework import serializers as s

from plane.models import PlaneModel


class PlaneSerializers(s.ModelSerializer):
    class Meta:
        model = PlaneModel
        fields = '__all__'
