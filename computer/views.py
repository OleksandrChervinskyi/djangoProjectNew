from typing import List
from django.forms import model_to_dict
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from computer.models import ComputerModel


# Create your views here. CRUD

class ComputerListCreateView(APIView):
    def get(self, *args, **kwargs):
        if self.request.query_params:
            query_keys = list(self.request.query_params.keys())
            selected_key = query_keys[0]  # brand, cpu, screen ...
            query_item: str = self.request.query_params[selected_key]  # Hp, Mac, Lenovo ...

            # str to int from query params
            int_or_str_query_item = int(query_item) if query_item.isdigit() else query_item

            all_list: List = ComputerModel.objects.values()
            filtered_list = list(filter(lambda value: value[selected_key] == int_or_str_query_item, all_list))

            # For not get empty list
            if len(filtered_list):
                return Response(filtered_list)

        # Without query params
        all_computers = ComputerModel.objects.all().values()
        return Response(all_computers, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data.dict()
        ComputerModel.objects.create(**data)

        return Response(data, status.HTTP_201_CREATED)


class ComputerRetrieveUpdateDeleteView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('This id not found', status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.get(pk=pk)

        return Response(model_to_dict(computer), status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        data = self.request.data.dict()
        ComputerModel.objects.filter(pk=pk).update(**data)
        return Response('Updated', status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.filter(pk=pk)
        computer.delete()
        return Response(status.HTTP_204_NO_CONTENT)
