from django.shortcuts import render
from .forms import RegistrationForm
# Create your views here.
def home(request):
    form = RegistrationForm()
    return render(request, 'profiles/index.html', {'form': form})