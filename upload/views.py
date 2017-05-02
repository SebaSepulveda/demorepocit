from django.views import generic
import os
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.db.models import Q
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from .models import Base, Down, MyModel, Uploader, Paquetes, Tags
from .forms import UserForm, DownloadForm, MyModelForm
import subprocess


class IndexView(generic.ListView):
	template_name='upload/index.html'
	context_object_name ='all_base'

	def get_queryset(self):
		return Base.objects.all()

class DataView(generic.ListView):
	template_name='upload/bases_de_datos.html'
	context_object_name ='all_base'
	
	def get_queryset(self):
		return Base.objects.all()
	

class ProjectView(generic.ListView):
	template_name='upload/project_form.html'
	context_object_name ='all_base'

	def get_queryset(self):
		return Base.objects.all()

class DetailView(generic.DetailView):
	model = Base
	template_name ='upload/detail.html'


class LinkView(generic.ListView):
	template_name='upload/link.html'
	context_object_name ='all_base'

	def get_queryset(self):
		return Base.objects.all()

class UploaderCreate(CreateView):
	model = Uploader
	fields = ['update','nombre_proyecto','razon_de_carga','tipo_de_datos','unidad_territorial','archivo','comentarios']
	success_url = reverse_lazy('upload:index')
	send_mail('Descarga CIT2', 'Descarga Disponible en Servidor.', 'vaalhk@gmail.com', ['seba.sepulveda88@gmail.com'], fail_silently=False)

class Paquetes(CreateView):
	model =Paquetes
	fields='upload/paquetes.html'

class Tags(CreateView):
	model=Tags
	fields='upload/tags.html'
	


class BaseCreate(CreateView):
	model = Base
	fields = ['name','project_name','zone','archivo']
	success_url = reverse_lazy('upload:index')
	send_mail('Descarga CIT2', 'Descarga Disponible en Servidor.', 'vaalhk@gmail.com', ['seba.sepulveda88@gmail.com'], fail_silently=False)
	


class DownCreate(CreateView):
	model = Base
	fields = ['name','project_name']
	success_url = reverse_lazy('upload:link')

class CreateMyModelView(CreateView):
	model=MyModel
	template_name='upload/down_form.html'
	#form_class=MyModelForm
	fields=['manzana', 'archivo','poligono']
	success_url=reverse_lazy('upload:link')


class UserFormView(View):
	form_class = UserForm
	template_name='upload/registration_form.html'
	# blank info
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})
	#process info	
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			#clean data
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user=authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('upload:index')

		return render(request, self.template_name, {'form': form})

