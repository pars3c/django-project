from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'profiles/home.html')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                print('super')
                user = form.save(commit=True)
                auth_login(request, user)
                return redirect('/profiles')
                
            else:
                print('NOT VALIDATED')
    return render(request, 'profiles/register.html', {'form': form})


def profile(request):
    args = {'user': request.user}
    return render(request, 'profiles/profile.html', args)