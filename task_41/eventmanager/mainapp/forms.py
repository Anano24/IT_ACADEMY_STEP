from django import forms
from .models import Event
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class EventForm(forms.ModelForm):

    class Meta:
        model = Event

        fields = ['title', 'description', 'date', 'location', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter The Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please Enter The Description'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please Enter The Location'}),
        }



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']



