from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import Turno
from .recordatorio import enviar_recordatorio_email

from django.contrib.auth.decorators import login_required, user_passes_test


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
