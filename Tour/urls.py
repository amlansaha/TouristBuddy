from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_selected_value, name='get_selected_value'),
    url(r'^(?P<source>[^\_]+)[_](?P<dest>[^\_]+)/$', views.retrieve, name='retrieve'),
    url(r'^([^\_]+[_][^\_]+)/(?P<source>[^\_]+)[_](?P<dest>[^\_]+)[_](?P<option>[^\_]+)/$', views.retrieve_details, name='retrieve_details'),
    url(r'^register$', views.user_register, name='user_register'),
    
    #user auth urls
    url(r'^login/$', 'django_test.views.login'),
    url(r'^auth/$', 'django_test.views.auth_view'),
    url(r'^logout/$', 'django_test.views.logout'),
    url(r'^loggedin/$', 'django_test.views.loggedin'),
    url(r'^invalid/$', 'django_test.views.invalid_login'),
]


