from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from cars.models import CarsModel
from cars.serializer import CarsSerializers


class CarsListCreateAPIView(ListCreateAPIView):
    serializer_class = CarsSerializers

    def get_queryset(self):
        queryset = CarsModel.objects.all()

        # Query
        autopark_id = self.request.query_params.get('autoParkId')
        if autopark_id:
            return queryset.filter(auto_park_id=autopark_id)

        return queryset


class CarsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarsSerializers
    queryset = CarsModel.objects.all()
