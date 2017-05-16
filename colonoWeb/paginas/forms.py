#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms

#Formulario usado en el cargado de la imagen.
from django.forms import widgets, Select


class UploadFileForm(forms.Form):
   archivo = forms.FileField()

#Formulario usado en la configuracion de los Parametros.
class Parametros(forms.Form):
   escala = forms.FloatField(label='Escala pixel x metro:',min_value=0.03)
   ruido = forms.IntegerField(label='Filtro de ruido:',min_value=0)
   proximidad=forms.FloatField(label='Proximidad:',min_value=0.0)
   capacidad=forms.DecimalField(label='Capacidad de Memoria:', min_value=0)
   multiArchivo=forms.NullBooleanField(label='MultiArchivos:', widget=Select(choices=[(True, "Sí"),(False, "No")]))
   nombreArchivo=forms.CharField(label='Nombre del Archivo shp ',widget=forms.TextInput)
