from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'body': "templating"}
    return render(request, 'first_app/index.html', context=my_dict)


def about(request):
    return HttpResponse('about me')