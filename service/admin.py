from django.contrib import admin

# Register your models here.
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_model', 'car_notes', 'car_number', 'year_old', 'service_type']