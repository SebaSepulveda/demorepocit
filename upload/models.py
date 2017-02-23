from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.utils.datastructures import MultiValueDictKeyError
import os

class Base(models.Model):
	name = models.CharField(max_length=250)
	project_name = models.CharField(max_length=250)
	zone = models.CharField(max_length=250)
	archivo = models.FileField(upload_to='media/')

	def __str__(self):
		return self.name + ' - ' + self.project_name

BOOL_CHOICES = (
    ('si','Si'),
    ('no','No'),
        
)
TIPO_CHOICES = (
    ('shapefile','Shapefile'),
        
)


class Uploader(models.Model):
	update = models.CharField(max_length=50, choices=BOOL_CHOICES, default='update')
	nombre_proyecto = models.CharField(max_length=250)
	razon_de_carga=models.CharField(max_length=250)
	tipo_de_datos=models.CharField(max_length=250, choices=TIPO_CHOICES,default='shapefile')
	unidad_regional=models.CharField(max_length=250)
	comentarios=models.CharField(max_length=250)
	archivo = models.FileField(upload_to='media/')





class Down(models.Model):
	nombre = models.CharField(max_length=250)
	proyecto= models.CharField(max_length=250)



class Project(models.Model):
	project =models.ForeignKey(Base, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=25)
	name= models.CharField(max_length=250)
	is_favorite=models.BooleanField(default=False)


	def __str__(self):
		return str(self.project_id)
COLOR_CHOICES = (
    ('iquique','01_Iquique_AltoHospicio_poligono'),
        
)
FILE_CHOICES = (
    ('shapefile','Shapefile'),
        
)
POLIGONO_CHOICES = (
    ('poligono','Poligono'),
        
)

class MyModel(models.Model):

	poligono = models.CharField(max_length=50, choices=POLIGONO_CHOICES, default='poligono')
	manzana = models.CharField(max_length=50, choices=COLOR_CHOICES, default='iquique')
	archivo= models.CharField(max_length=50, choices=FILE_CHOICES, default='shapefile')
