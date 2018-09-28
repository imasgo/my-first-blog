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
    url(r'^all/$', views.all, name='letopis'),
    url(r'^show_note/(?P<pk>\d+)/$', views.show_note, name='show_note'),
    url(r'^add_note/', views.add_note, name='add_note'),
    url(r'^1112-1122/$', views.one, name='1112-1122'),
    url(r'^852-963/$', views.eightfivetwo, name='852-963'),
    url(r'^XII/$', views.twelve, name='XII век'),
    url(r'^jews/$', views.jews, name='Еврейско-хазарская переписка Х века'),
    url(r'^cambridge/$', views.cambridge, name='Киевское письмо и Кембриджский документ'),
    url(r'^novgorod/$', views.novgorod, name='Новгород'),
    url(r'^saga/$', views.saga, name='Сага об Олаве Трюгвассоне'),
    url(r'^sophia/$', views.sophia, name='София Киевская'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
