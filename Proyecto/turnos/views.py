from django.shortcuts import render, redirect
from .forms import DisponibilidadForm
from django.shortcuts import get_object_or_404
from .models import Doctor, Disponibilidad

def crear_disponibilidad(request):
    if request.method == 'POST':
        form = DisponibilidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_disponibilidad')
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
            return redirect('ver_disponibilidad')
    else:
        form = DisponibilidadForm(instance=disponibilidad)
    return render(request, 'turnos/editar_disponibilidad.html', {'form': form})

def borrar_disponibilidad(request, id_disponibilidad):
    disponibilidad = get_object_or_404(Disponibilidad, id_disponibilidad=id_disponibilidad)
    if request.method == 'POST':
        disponibilidad.delete()
        return redirect('ver_disponibilidad')
    return render(request, 'turnos/borrar_disponibilidad.html', {'disponibilidad': disponibilidad})
