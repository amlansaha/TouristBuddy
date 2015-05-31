from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_selected_value, name='get_selected_value'),
    url(r'^(?P<source>[^\_]+)[_](?P<dest>[^\_]+)/$', views.retrieve, name='retrieve'),
    url(r'^([^\_]+[_][^\_]+)/(?P<source>[^\_]+)[_](?P<dest>[^\_]+)[_](?P<option>[^\_]+)/$', views.retrieve_details, name='retrieve_details'),
    url(r'^register$', views.user_register, name='user_register'),
    
    #user auth urls
    url(r'^login$', views.user_login),
    url(r'^login/(?P<email>[^\_]+)[_](?P<pw>[^\_]+)$', views.user_login),
    url(r'^logout/$', views.user_logout),
    url(r'^loggedin/$', views.user_loggedin),
#    url(r'^invalid/$', views.user.invalid),
]


