from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_selected_value, name='get_selected_value'),
    url(r'^(?P<source>[^\_]+)[_](?P<dest>[^\_]+)/$', views.retrieve, name='retrieve'),
    url(r'^([^\_]+[_][^\_]+)/(?P<source>[^\_]+)[_](?P<dest>[^\_]+)[_](?P<option>[^\_]+)/$', views.retrieve_details, name='retrieve_details'),
    url(r'^register$', views.user_register, name='user_register')
]


