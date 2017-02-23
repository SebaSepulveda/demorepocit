from django.contrib.auth.models import User
from django import forms
from .models import Down, MyModel
from django.forms import ModelForm

class UserForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	
	class Meta:
		model=User
		fields= ['username', 'email','password']
class DownloadForm(forms.ModelForm):
	class Meta:
		model = Down
		fields=['nombre','proyecto']

class MyModelForm(ModelForm):
    class Meta:
        model = MyModel
        fields = ['manzana', 'archivo','poligono']