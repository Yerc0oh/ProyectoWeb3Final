# -*- coding: utf-8 -*-
import logging
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from email.header import Header

logger = logging.getLogger(__name__)

def enviar_recordatorio_email(turno):
    asunto = Header("Recordatorio de turno médico", 'utf-8')

    contexto = {
        "doctor": turno.id_doctor,
        "paciente": turno.id_paciente,
        "fecha_hora": turno.fecha_hora.strftime('%d/%m/%Y a las %H:%M'),
    }

    mensaje_html = render_to_string("turnos/recordatorio_turno.html", contexto)

    destinatario = [turno.id_paciente.email]

    try:
        email = EmailMultiAlternatives(
            subject=asunto,
            body="Este es un recordatorio de su turno médico.",  # texto plano
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=destinatario,
        )
        email.encoding = 'utf-8'
        email.attach_alternative(mensaje_html, "text/html")
        email.send(fail_silently=False)
        logger.info(f"Correo de recordatorio enviado exitosamente a {turno.id_paciente.email}")
    except Exception as e:
        logger.error(f"Error al enviar correo a {turno.id_paciente.email}: {str(e)}")
        raise