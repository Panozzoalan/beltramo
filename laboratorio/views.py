from django.shortcuts import render, redirect,get_object_or_404
from laboratorio.models import Paciente
from laboratorio.models import Medico, Especialidad
from laboratorio.models import Estudio_medico
from .forms import PacienteForm
from .forms import MedicoForm


def index(request):
   return render(request, 'laboratorio/index.html', {})

def paciente(request):
   pacientes=Paciente.objects.all()
   return render(request, 'laboratorio/pacientes_list.html', {'pacientes':pacientes})


def medico(request):
   especialidades=Especialidad.objects.all()
   return render(request, 'laboratorio/medicos_list.html', {'especialidades':especialidades})

def estudios_medicos(request):
   estudios=Estudio_medico.objects.all()
   return render(request, 'laboratorio/estudios_list.html', {'estudios':estudios})

def contacto(request):
   return render(request, 'laboratorio/contacto.html',{})

def paciente_new(request):
        print(request) 
        if request.method == "POST":
            form = PacienteForm(request.POST, request.FILES)
            if form.is_valid():
                paciente = form.save(commit=False)
                paciente.save()
                pacientes = Paciente.objects.all()
                return render(request, 'laboratorio/pacientes_list.html',{'pacientes': pacientes})
        else:
            form = PacienteForm()
        return render(request, 'laboratorio/paciente_edit.html', {'form': form})


def paciente_edit(request,pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        if request.method == "POST":
            form = PacienteForm(request.POST, request.FILES,instance=paciente)
            if form.is_valid():
                paciente = form.save(commit=False)
                paciente.save()
                pacientes = Paciente.objects.all()
                return render(request, 'laboratorio/pacientes_list.html',{'pacientes': pacientes})
        else:
            form = PacienteForm(instance=paciente)
        return render(request, 'laboratorio/paciente_edit.html', {'form': form})

def medico_edit(request,pk):
        medico = get_object_or_404(Medico, pk=pk)
        if request.method == "POST":
            form = MedicoForm(request.POST, request.FILES,instance=medico)
            if form.is_valid():
                medico = form.save(commit=False)
                medico.save()
                medicos = Medico.objects.all()
                return render(request, 'laboratorio/medicos_list.html',{'medicos': medicos})
        else:
            form = MedicoForm(instance=medico)
        return render(request, 'laboratorio/medico_edit.html', {'form': form})


def medicos_por_especialidad(request,pk):
        medicos = Medico.objects.filter(especialidad=pk)
        return render(request, 'laboratorio/medicos_por_especialidad.html',{'medicos': medicos})

def pacientes_por_estudios(request,pk):
        pacientes = Paciente.objects.filter(estudio=pk)
        return render(request, 'laboratorio/pacientes_por_estudios.html',{'pacientes': pacientes})




