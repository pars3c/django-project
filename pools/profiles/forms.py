from django import forms

class RegistrationForm(forms.Form):
    name = forms.CharField(min_length=2, max_length=100)
    age = forms.IntegerField(min_value=18, max_value=99)
    CHOICES = (('Option 1', 'Option 3'),('Option 2', 'Option 2'),)
    field = forms.ChoiceField(choices=CHOICES)