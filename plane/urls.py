from django.urls import path

from plane.views import PlaneListCreate, PlaneRetrieveUpdateDelete

urlpatterns = [
    path('', PlaneListCreate.as_view(), name='get_create_planes'),
    path('/<int:pk>', PlaneRetrieveUpdateDelete.as_view(), name='plane retrieve_update_delete')

]
