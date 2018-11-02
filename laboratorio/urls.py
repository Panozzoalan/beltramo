from django.conf.urls import include, url
from . import views

from django.conf.urls import static

urlpatterns = [
   url(r'^$', views.index), 
   url(r'index$', views.index, name='laboratorio'),
   url(r'paciente$', views.paciente, name='paciente') ,	 
   url(r'medico$', views.medico, name='medico') ,
   url(r'estudios_medicos$', views.estudios_medicos, name='estudios_medicos') ,
   url(r'contacto$', views.contacto, name='contacto'),
   url(r'^pacientenew/$', views.paciente_new, name='paciente_new'),
   url(r'^paciente/(?P<pk>[0-9]+)/edit/$', views.paciente_edit, name='paciente_edit'),
   url(r'^especialidad/(?P<pk>[0-9]+)/$', views.medicos_por_especialidad, name='filtrado'),
#   url(r'^/(?P<pk>[0-9]+)/$', views.medicos_por_especialidad, name='filtrado'),
   url(r'^estudios/(?P<pk>[0-9]+)/$', views.pacientes_por_estudios, name='filtradopacientes'),



	   
   
]
