@echo off
cd /d "%~dp0"
call ..\env\Scripts\activate.bat
python manage.py enviar_recordatorios
pause