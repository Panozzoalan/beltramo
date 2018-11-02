from django import forms
from .models import Paciente
from .models import Medico

class PacienteForm(forms.ModelForm):

    class Meta:
        model = Paciente
        fields = ('nombre_y_apellido', 'dni','telefono','fecha_nacimiento',)


class MedicoForm(forms.ModelForm):

    class Meta:
        model = Medico
        fields = ('nombre_y_apellido', 'dni','telefono','especialidad',)
