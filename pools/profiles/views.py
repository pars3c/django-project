from django.shortcuts import render
from profiles.forms import UserForm
# Create your views here.
def home(request):
    form = UserForm()
    if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                print('VALIDATED')
                
            else:
                print('NOT VALIDATED')
    return render(request, 'profiles/index.html', {'form': form})