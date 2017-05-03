from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.utils.datastructures import MultiValueDictKeyError
from taggit.managers import TaggableManager
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
    ('csv', 'CSV'),
        
)
TIPO_REGIONAL = (
    ('region','Region'),
    ('provincia','Provincia'),
    ('comuna','Comuna'),
    ('distrito','Distrito'),
    ('manzana','Manzana'),
        
)
PAQUETES = (
    ('R1','Region 1'),
    ('R2','Region 2'),
    ('R3','Region 3'),
    ('R4','Region 4'),
    ('R5','Region 5'),
        
)

class Paquetes(models.Model):
	tipo_paquetes=models.CharField(max_length=250, choices=PAQUETES, default='R1')
	#tipo_de_datos=models.CharField(max_length=250, choices=TIPO_CHOICES,default='shapefile')
	



class Tags(models.Model):
	Tags=models.CharField(max_length=250)

class Uploader(models.Model):
	update = models.CharField(max_length=50, choices=BOOL_CHOICES, default='update')
	nombre_proyecto = models.CharField(max_length=250)
	razon_de_carga=models.CharField(max_length=250)
	tipo_de_datos=models.CharField(max_length=250, choices=TIPO_CHOICES,default='shapefile')
	unidad_territorial=models.CharField(max_length=100, choices=TIPO_REGIONAL, default='region')
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
