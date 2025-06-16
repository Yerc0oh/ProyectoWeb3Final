
from .models import Doctor
from .models import Paciente
from .forms import DoctorForm, PacienteForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Turno
from .recordatorio import enviar_recordatorio_email
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import DisponibilidadForm
from .models import Disponibilidad
from .models import Especialidad
from .forms import TurnoForm
from .forms import *
# Create your views here.
def lista_doctores(request):
    doctores = Doctor.objects.select_related('id_especialidad').all()
    return render(request, 'turnos/lista_doctor.html', {'doctores': doctores})


def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'turnos/lista_paciente.html', {'pacientes': pacientes})


def registrar_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:lista_doctores')  # o alguna otra vista
    else:
        form = DoctorForm()
    return render(request, 'turnos/doctor_form.html', {'form': form})

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:paciente_list')  # o alguna otra vista
    else:
        form = PacienteForm()
    return render(request, 'turnos/paciente_form.html', {'form': form})

def editar_paciente(request, id_paciente):
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('turnos:paciente_list')  # Redirige a la lista de pacientes
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'turnos/paciente_form.html', {'form': form})

def eliminar_paciente(request, id_paciente):
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    if request.method == 'POST':
        paciente.delete()
        return redirect('turnos:paciente_list')  # Redirige a la lista de pacientes
    return render(request, 'turnos/eliminar_paciente.html', {'paciente': paciente})

def editar_doctor(request, id_doctor):
    doctor = get_object_or_404(Doctor, id_doctor=id_doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('turnos:lista_doctores')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'turnos/doctor_form.html', {'form': form, 'doctor': doctor})

def eliminar_doctor(request, id_doctor):
    doctor = get_object_or_404(Doctor, id_doctor=id_doctor)
    if request.method == 'POST':
        doctor.delete()
        return redirect('turnos:lista_doctores')
    return render(request, 'turnos/eliminar_doctor.html', {'doctor': doctor})



def recordatorio(request):
    ahora = timezone.now()
    desde = ahora + timedelta(hours=23, minutes=55)
    hasta = ahora + timedelta(hours=25)

    turnos_pendientes = Turno.objects.filter(
        fecha_hora__gte=desde,
        fecha_hora__lte=hasta,
        recordatorio_enviado=False
    )

    if request.method == "POST":
        if turnos_pendientes.exists():
            enviados = 0
            for turno in turnos_pendientes:
                try:
                    enviar_recordatorio_email(turno)
                    turno.recordatorio_enviado = True
                    turno.fecha_recordatorio = timezone.now()
                    turno.save()
                    enviados += 1
                except Exception as e:
                    messages.error(request, f"Error al enviar a {turno.id_paciente.email}: {e}")
            messages.success(request, f"Se enviaron {enviados} recordatorios correctamente.")
        else:
            messages.info(request, "No hay recordatorios pendientes.")

    else:
        if turnos_pendientes.exists():
            messages.info(request, "Hay recordatorios pendientes.")
        else:
            messages.info(request, "No hay recordatorios pendientes.")

    return render(request, 'turnos/recordatorio.html')

def crear_disponibilidad(request):
    if request.method == 'POST':
        form = DisponibilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:ver_disponibilidad')
    else:
        form = DisponibilidadForm()
    return render(request, 'turnos/crear_disponibilidad.html', {'form': form})

def ver_disponibilidad(request):
    doctor_nombre = request.GET.get('doctor_nombre')
    doctores = Doctor.objects.all().order_by('nombre', 'apellido')

    if doctor_nombre:
        disponibilidades = Disponibilidad.objects.filter(
            id_doctor__nombre__icontains=doctor_nombre
        ).order_by('id_doctor', 'dia_semana', 'hora_inicio')
    else:
        disponibilidades = Disponibilidad.objects.all().order_by('id_doctor', 'dia_semana', 'hora_inicio')

    return render(request, 'turnos/ver_disponibilidad.html', {
        'disponibilidades': disponibilidades,
        'doctores': doctores,
        'doctor_nombre': doctor_nombre,
    })
 
def editar_disponibilidad(request, id_disponibilidad):
    disponibilidad = get_object_or_404(Disponibilidad, id_disponibilidad=id_disponibilidad)
    if request.method == 'POST':
        form = DisponibilidadForm(request.POST, instance=disponibilidad)
        if form.is_valid():
            form.save()
            return redirect('turnos:ver_disponibilidad')
    else:
        form = DisponibilidadForm(instance=disponibilidad)
    return render(request, 'turnos/editar_disponibilidad.html', {'form': form})

def borrar_disponibilidad(request, id_disponibilidad):
    disponibilidad = get_object_or_404(Disponibilidad, id_disponibilidad=id_disponibilidad)
    if request.method == 'POST':
        disponibilidad.delete()
        return redirect('turnos:ver_disponibilidad')
    return render(request, 'turnos/borrar_disponibilidad.html', {'disponibilidad': disponibilidad})

def inicio(request):
    return render(request, 'turnos/inicio.html')
def lista_turnos(request):
    turnos = Turno.objects.select_related('id_doctor', 'id_paciente').all()
    return render(request, 'turnos/lista_turnos.html', {'turnos': turnos})

def registrar_turno(request):
    if request.method == 'POST':
        form = TurnoForm(request.POST)
        if form.is_valid():
            turno = form.save(commit=False)
            turno.recordatorio_enviado = False  
            turno.save()
            return redirect('turnos:lista_turnos')  # o alguna otra vista
    else:
        form = TurnoForm()
    return render(request, 'turnos/turno_form.html', {'form': form})

def editar_turno(request, id_turno):
    turno = get_object_or_404(Turno, id_turno=id_turno)
    if request.method == 'POST':
        form = TurnoForm(request.POST, instance=turno)
        if form.is_valid():
            form.save()
            return redirect('turnos:lista_turnos')  # Redirige a la lista de turnos
    else:
        form = TurnoForm(instance=turno)
    return render(request, 'turnos/turno_form.html', {'form': form})

def eliminar_turno(request, id_turno):
    turno = get_object_or_404(Turno, id_turno=id_turno)
    if request.method == 'POST':
        turno.delete()
        return redirect('turnos:lista_turnos')  # Redirige a la lista de turnos
    return render(request, 'turnos/eliminar_turno.html', {'turno': turno})

def registrar_especialidad(request):
    if request.method == 'POST':
        form = EspecialidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:lista_especialidades')  # o alguna otra vista
    else:
        form = EspecialidadForm()
    return render(request, 'turnos/especialidad_form.html', {'form': form})

def editar_especialidad(request, id_especialidad):
    especialidad = get_object_or_404(Especialidad, id_especialidad=id_especialidad)
    if request.method == 'POST':
        form = EspecialidadForm(request.POST, instance=especialidad)
        if form.is_valid():
            form.save()
            return redirect('turnos:lista_especialidades')  # Redirige a la lista de especialidades
    else:
        form = EspecialidadForm(instance=especialidad)
    return render(request, 'turnos/especialidad_form.html', {'form': form})
def eliminar_especialidad(request, id_especialidad):
    especialidad = get_object_or_404(Especialidad, id_especialidad=id_especialidad)
    if request.method == 'POST':
        especialidad.delete()
        return redirect('turnos:lista_especialidades')  # Redirige a la lista de especialidades
    return render(request, 'turnos/eliminar_especialidad.html', {'especialidad': especialidad})

def lista_especialidades(request):
    especialidades = Especialidad.objects.all()
    return render(request, 'turnos/lista_especialidades.html', {'especialidades': especialidades})
