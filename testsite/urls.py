from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
# from .views import Gramota

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gramota/$', views.gramota, name='gramota'),
    url(r'^show_gramota/(?P<pk>\d+)/$', views.show_gramota, name='show_gramota'),
    url(r'^show_gramota/(?P<pk>\d+)/update_gramota/$', views.update_gramota, name='update_gramota'),
    url(r'^symbols_panel/$', views.symbols_panel, name='symbols_panel'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
