from django.urls import path

from plane.views import PlaneListCreateAPIView, PlaneRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', PlaneListCreateAPIView.as_view(), name='plane_list_create'),
    path('/<int:pk>', PlaneRetrieveUpdateDestroyAPIView.as_view(), name='plane_retrieve_update_delete')
]
