# coding=utf-8

from django.db import models

class Games(models.Model):
    titulo = models.CharField(max_length=255)
    plataformas = models.CharField(max_length=255)
