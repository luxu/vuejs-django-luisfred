# coding=utf-8

from django.contrib import admin
from .models import Games
from .forms import GamesAdmin

class GamesAdmin(admin.ModelAdmin):
    list_display = ['titulo','plataformas']
    search_fields = ['titulo', 'plataformas']


admin.site.register(Games, GamesAdmin)
