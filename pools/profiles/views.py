from django.shortcuts import render, redirect
#from profiles.forms import UserForm
#from profiles.models import UserProfile
from django.contrib.auth.models import User
from profiles.forms import UserCreateForm
# Create your views here.
def home(request):
    return render(request, 'profiles/home.html')

def register(request):
    form = UserCreateForm()
    if request.method == 'POST':
            form = UserCreateForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return redirect('/profiles')
                
            else:
                print('NOT VALIDATED')
    return render(request, 'profiles/register.html', {'form': form})


def profile(request):
    args = {'user': request.user}
    return render(request, 'profiles/profile.html', args)