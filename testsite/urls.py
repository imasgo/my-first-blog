from django.conf.urls import url
from . import views
# from .views import Gramota

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gramota/$', views.gramota, name='gramota'),
    url(r'^show_gramota/(?P<pk>\d+)/$', views.show_gramota, name='show_gramota'),
    url(r'^show_gramota/(?P<pk>\d+)/update_gramota/$', views.update_gramota, name='update_gramota')
]