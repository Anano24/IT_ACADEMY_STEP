from django import forms
from .models import Event, Attendee


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



class AttendeeForm(forms.ModelForm):

    class Meta:
        model = Attendee

        fields = ['name', 'email', 'event']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pleace Enter The Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }