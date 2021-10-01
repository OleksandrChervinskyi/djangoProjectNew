from django.urls import path

from autopark.views import AutoParkRetrieveUpdateDestroyAPIView, AutoParkListCreateAPIView
from cars.views import CarsListCreateAPIView

urlpatterns = [
    path('', AutoParkListCreateAPIView.as_view(), name='auto-park_list_create'),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyAPIView.as_view(), name='auto-park_retrieve_update_destroy'),
    path('/<int:pk>/cars', CarsListCreateAPIView.as_view(), name='create_cars_by_auto-park_id')
]
