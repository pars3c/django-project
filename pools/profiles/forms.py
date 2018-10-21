from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    super_duper = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "super_duper", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.super_duper = self.cleaned_data["super_duper"]
        if commit:
            user.save()
        return user