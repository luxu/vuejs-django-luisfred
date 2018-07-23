# coding=utf-8

from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Games

class GamesAdmin(forms.ModelForm):

    class Meta:
        model = Games
        fields = ['titulo', 'plataformas']
