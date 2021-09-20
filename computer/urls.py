from django.urls import path

from computer.views import ComputerListCreateView, ComputerRetrieveUpdateDeleteView

urlpatterns = [
    path('', ComputerListCreateView.as_view(), name='Get and Create computers'),
    path('/<int:pk>', ComputerRetrieveUpdateDeleteView.as_view(), name='Retrieve Update Delete Computers')
]
