from django.urls import path
from .views import CarListCreateView, CarRetriveUpdateDeleteView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car list create and delete'),
    path('/<int:pk>', CarRetriveUpdateDeleteView.as_view(), name='car retrive delete')
]
