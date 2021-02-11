from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Car
from django.http import Http404


def home(request):
    # return HttpResponse('<p> home view </p>')
    cars = Car.objects.all()
    return render(request, 'home.html', {'cars':'cars'})

def car_detail(request,id):
    # return HttpResponse('<p> car details</p>')
    try:
        car = Car.objects.get(id = id)
    except Car.DoesNotExist:
        raise Http404("Car not Found")

    return render(request, 'car_detail.html',{'car':'car'})