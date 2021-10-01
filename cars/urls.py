from django.urls import path

from cars.views import CarsListCreateAPIView, CarsRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CarsListCreateAPIView.as_view(), name='cars_list_create'),
    path('/<int:pk>', CarsRetrieveUpdateDestroyAPIView.as_view(), name='cars_retrieve_update_destroy')
]
