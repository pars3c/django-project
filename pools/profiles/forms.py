from django import forms
from django.core import validators
from profiles.models import UserProfile
class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"