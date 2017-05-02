from django.conf.urls import url
from . import views

app_name = 'upload'

urlpatterns = [
	# /upload/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^project/$', views.ProjectView.as_view(), name='project'),
    url(r'^database/$', views.DataView.as_view(), name='data'),
        
    #url(r'^submit/(?P<path>.*)$', views.download),


    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #url(r'^login_user/$', views.login_user, name='login_user'),
    #url(r'^logout_user/$', views.logout_user, name='logout_user'),


    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

	url(r'^base/add/$', views.UploaderCreate.as_view(), name='base-add'),

    url(r'^download/$', views.CreateMyModelView.as_view(), name='download'),
    url(r'^link/$', views.LinkView.as_view(), name='link'),
    url(r'^paquetes/$', views.Paquetes.as_view(), name='paquetes'),
    url(r'^tags/$', views.Tags.as_view(), name='tags')


]
