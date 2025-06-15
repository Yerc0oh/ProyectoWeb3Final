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

# Create your views here.
def lista_doctores(request):
    doctores = Doctor.objects.select_related('id_especialidad').all()
    return render(request, 'lista_doctor.html', {'doctores': doctores})


def paciente_list(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_paciente.html', {'pacientes': pacientes})


def registrar_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:lista_doctores')  # o alguna otra vista
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'form': form})

def registrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('turnos:paciente_list')  # o alguna otra vista
    else:
        form = PacienteForm()
    return render(request, 'paciente_form.html', {'form': form})

def editar_paciente(request, id_paciente):
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('turnos:paciente_list')  # Redirige a la lista de pacientes
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'paciente_form.html', {'form': form})

def eliminar_paciente(request, id_paciente):
    paciente = get_object_or_404(Paciente, id_paciente=id_paciente)
    if request.method == 'POST':
        paciente.delete()
        return redirect('turnos:paciente_list')  # Redirige a la lista de pacientes
    return render(request, 'eliminar_paciente.html', {'paciente': paciente})

def editar_doctor(request, id_doctor):
    doctor = get_object_or_404(Doctor, id_doctor=id_doctor)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('turnos:lista_doctores')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_form.html', {'form': form, 'doctor': doctor})

def eliminar_doctor(request, id_doctor):
    doctor = get_object_or_404(Doctor, id_doctor=id_doctor)
    if request.method == 'POST':
        doctor.delete()
        return redirect('turnos:lista_doctores')
    return render(request, 'eliminar_doctor.html', {'doctor': doctor})

def recordatorio(request):
    ahora = timezone.now()
    desde = ahora + timedelta(hours=23, minutes=55)
    hasta = ahora + timedelta(hours=25)

    turnos = Turno.objects.filter(
        fecha_hora__gte=desde,
        fecha_hora__lte=hasta,
        recordatorio_enviado=False
    )

    if not turnos.exists():
        messages.info(request, "No hay recordatorios pendientes.")
    else:
        enviados = 0
        for turno in turnos:
            try:
                enviar_recordatorio_email(turno)
                turno.recordatorio_enviado = True
                turno.fecha_recordatorio = timezone.now()
                turno.save()
                enviados += 1
            except Exception as e:
                messages.error(request, f"Error al enviar a {turno.id_paciente.email}: {e}")
        messages.success(request, f"Se enviaron {enviados} recordatorios correctamente.")

    return render(request, 'turnos/recordatorio.html')

