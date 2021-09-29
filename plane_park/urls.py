from django.urls import path

from plane_park.views import PlaneParkListCreate

urlpatterns = [
    path('', PlaneParkListCreate.as_view(), name='plane_park_list_create')
]
