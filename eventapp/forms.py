from django import forms
from .models import Profile,Event,Location
from django.contrib.auth.models import User
from django.forms import ModelForm


class NewProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude =['user']

class NewLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        exclude = ['user','project']

class NewEventForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['user']   

