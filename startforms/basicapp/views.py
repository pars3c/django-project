from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime

def home(request):
    return render(request, 'basicapp/index.html')

