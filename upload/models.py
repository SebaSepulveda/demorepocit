from __future__ import unicode_literals

from django.db import models

class Base(models.Model):
	name = models.CharField(max_length=250)
	project_name= models.CharField(max_length=250)
	zone =models.CharField(max_length=250)
	archivo = models.FileField(upload_to='media/')

	def __str__(self):
		return self.name + ' - ' + self.project_name
class Down(models.Model):
	nombre = models.CharField(max_length=250)
	proyecto= models.CharField(max_length=250)
	
	#archivo = models.FileField()

	def __str__(self):
		return self.name + ' - ' + self.project_name

class Project(models.Model):
	project =models.ForeignKey(Base, on_delete=models.CASCADE)
	file_type = models.CharField(max_length=25)
	name= models.CharField(max_length=250)
	is_favorite=models.BooleanField(default=False)


	def __str__(self):
		return str(self.project_id)

