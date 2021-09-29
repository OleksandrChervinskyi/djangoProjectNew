from rest_framework import serializers as s

from plane.serializers import PlaneSerializer
from plane_park.models import PlaneParkModel


class PlaneParkSerializer(s.ModelSerializer):
    planes = PlaneSerializer(many=True, read_only=True)

    class Meta:
        model = PlaneParkModel
        fields = ('id', 'brand', 'city', 'created_at', 'planes')
