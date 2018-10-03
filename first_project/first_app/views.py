from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import AccessRecord, Webpage, Topic

# Create your views here.
def index(request):
    access_records = AccessRecord.objects.all
    my_dict = {'access_records': access_records}
    return render(request, 'first_app/index.html', context=my_dict)


def about(request):
    return HttpResponse('about me')