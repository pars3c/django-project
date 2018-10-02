from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'super': "duper"}
    return render(request, 'apptwo/index.html', context=my_dict)
