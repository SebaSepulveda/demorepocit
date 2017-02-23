from django.contrib import admin
from .models import Base, Project, Down, Uploader

admin.site.register(Uploader)
admin.site.register(Project)
admin.site.register(Down)