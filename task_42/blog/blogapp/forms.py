from django import forms
from .models import Blog
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog

        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Please enter the title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter the content'}),  
        }



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User

        fields = ['username', 'email', 'password1', 'password2']