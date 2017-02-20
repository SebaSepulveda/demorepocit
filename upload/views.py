from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.db.models import Q
from django.views.generic import View
from django.core.urlresolvers import reverse_lazy
from .models import Base, Down
from .forms import UserForm

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
	template_name='upload/detail.html'

class BaseCreate(CreateView):
	model = Base
	fields =['name','project_name','zone','archivo']
	success_url=reverse_lazy('upload:index')

class DownCreate(CreateView):
	model = Down
	fields =['nombre','proyecto']
	success_url=reverse_lazy('upload:index')


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

