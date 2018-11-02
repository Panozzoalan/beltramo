from django.contrib import admin
from .models import Paciente
from .models import Medico
from .models import Estudio_medico
from .models import Especialidad

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Estudio_medico)
admin.site.register(Especialidad)

 
