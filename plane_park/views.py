from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from plane_park.models import PlaneParkModel
from plane_park.serializer import PlaneParkSerializer


class PlaneParkListCreate(ListCreateAPIView):
    serializer_class = PlaneParkSerializer
    queryset = PlaneParkModel.objects.all()
