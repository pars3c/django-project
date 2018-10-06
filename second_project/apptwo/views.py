from django.shortcuts import render
from django.http import HttpResponse
from apptwo.models import Car

# Create your views here.
def index(request):
    carros = Car.objects.all
    cars = {'carros': carros}
    my_dict = {'super': "duper"}
    return render(request, 'apptwo/index.html', context=cars)
