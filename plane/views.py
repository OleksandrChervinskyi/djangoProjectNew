from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from plane.models import PlaneModel
from plane.serializers import PlaneSerializer


# Create your views here.


class PlaneListCreate(APIView):
    def get(self, *args, **kwargs):
        data = PlaneModel.objects.all()
        serialized = PlaneSerializer(data, many=True)
        return Response(serialized.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = PlaneSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class PlaneRetrieveUpdateDelete(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        if not PlaneModel.objects.filter(pk=pk).exists():
            return Response(f'Not found pane by this id - {pk}')
        plane = PlaneModel.objects.get(pk=pk)
        serializer = PlaneSerializer(plane)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = PlaneModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found this id', status.HTTP_404_NOT_FOUND)
        plane = PlaneModel.objects.filter(pk=pk).first()
        data = self.request.data
        serializer = PlaneSerializer(plane, data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exist = PlaneModel.objects.filter(pk=pk).exists()
        if not exist:
            return Response('Not found this id', status.HTTP_404_NOT_FOUND)
        plane = PlaneModel.objects.filter(pk=pk)
        plane.delete()
        return Response(status.HTTP_204_NO_CONTENT)
