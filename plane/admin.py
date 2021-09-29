from django.contrib import admin

from .models import PlaneModel


# Register your models here.

@admin.register(PlaneModel)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'country_of_manufacture')
