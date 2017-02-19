from django.conf.urls import url
from . import views

app_name = 'upload'

urlpatterns = [
	
	# /upload/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^project/$', views.ProjectView.as_view(), name='project'),
    url(r'^database/$', views.DataView.as_view(), name='data'),



    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #url(r'^login_user/$', views.login_user, name='login_user'),
    #url(r'^logout_user/$', views.logout_user, name='logout_user'),


    #/upload/<base_id>
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

	url(r'^base/add/$', views.BaseCreate.as_view(), name='base-add')    


]
