from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from plane.models import PlaneModel
from plane.serializers import PlaneSerializers


class PlaneListCreateAPIView(ListCreateAPIView):
    serializer_class = PlaneSerializers
    queryset = PlaneModel.objects.all()


class PlaneRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlaneSerializers
    queryset = PlaneModel.objects.all()
