from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from autopark.models import AutoParkModel
from autopark.serializer import AutoParkSerializers


class AutoParkListCreateAPIView(ListCreateAPIView):
    serializer_class = AutoParkSerializers

    # def get_queryset(self):
    #     queryset = AutoParkModel.objects.all()
    #     return queryset
    #
    # def get(self, request, *args, **kwargs):
    #     auto_park_id = kwargs.get('pk')
    #     print(auto_park_id)
    #     return super().get(request, *args, **kwargs)


class AutoParkRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AutoParkSerializers
    queryset = AutoParkModel.objects.all()
