from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from profiles.forms import UserForm, UserProfileInfoForm


from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse


from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'profiles/home.html')

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic'in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'profiles/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print('worked')
                return redirect('/profiles/profile')
            else:
                return HttpResponse("YOU ARE NOT LOGGED IN!")
        print("Someone tried to login and failed!")
        return HttpResponse("invalid details")
    else:
        return render(request, "profiles/login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'profiles/profile.html', args)