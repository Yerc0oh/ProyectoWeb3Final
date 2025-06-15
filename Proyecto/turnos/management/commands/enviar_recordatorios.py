from django.core.management.base import BaseCommand
from turnos.models import Turno
from turnos.recordatorio import enviar_recordatorio_email
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Envia recordatorios por email para turnos programados 24h antes'

    def handle(self, *args, **kwargs):
        ahora = timezone.now()
        desde = ahora + timedelta(hours=23, minutes=55)
        hasta = ahora + timedelta(hours=25)


        turnos = Turno.objects.filter(
            fecha_hora__gte=desde,
            fecha_hora__lte=hasta,
            recordatorio_enviado=False
        )

        if not turnos.exists():
            self.stdout.write("No hay recordatorios pendientes.")
            return

        for turno in turnos:
            try:
                enviar_recordatorio_email(turno)
                turno.recordatorio_enviado = True
                turno.fecha_recordatorio = timezone.now()
                turno.save()
                self.stdout.write(f"Recordatorio enviado a {turno.id_paciente.email}")
            except Exception as e:
                self.stderr.write(f"Error al enviar a {turno.id_paciente.email}: {e}")
