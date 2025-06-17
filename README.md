# 🏥 Grupo 9 - Sistema de Turnos Médicos

## 👥 Nómina de integrantes

| Nombre completo                   | C.I.       | Nº Lista |
|----------------------------------|------------|----------|
| Calderón Calle Abed Yeray        | 12864956   | 27       |
| Callisaya Suarez Jose Fernando   | 9151092    | 33       |
| Conde Oquendo Maya Bettzy        | 10018614   | 58       |
| Mamani Huanca Dilan Alvaro       | 9870018    | 118      |
| Masco Vargas Melani              | 13844737   | 131      |

---

## ⚙️ Instrucciones importantes

### 🔹 Entorno Virtual
Este repositorio **no contiene un entorno virtual (`venv/`)**, por lo tanto debe ser creado manualmente:

```bash
python -m venv venv
source venv/bin/activate      # En Linux/Mac
venv\Scripts\activate.bat     # En Windows
pip install -r requirements.txt
```

---

### 📧 Recordatorios por email

Para que los recordatorios sean enviados correctamente por correo electrónico, **seguir el tutorial que se encuentra en el informe del proyecto**, o ver el video elaborado por **Melani Masco Vargas**, específicamente la sección de configuración de envío de correos.

---

### 🔐 Usuarios por defecto

| Usuario | Contraseña | Tipo de usuario  |
|---------|------------|------------------|
| Maria   | cba12345   | Usuario normal   |
| Carlos  | cba12345   | Administrador    |

> ⚠️ La base de datos **no contiene un superusuario de Django**.  
> Si se requiere acceso al panel de administración (`/admin`), deberá crearse con:

```bash
python manage.py createsuperuser
```

**Nota:** El usuario “Carlos” tiene permisos administrativos dentro del sistema, pero no puede acceder al panel `/admin`.

---

### 📦 Descarga de la última versión

- Última versión disponible como **tag `v1.1Final`** en este repositorio.
- También puede descargarse en formato `.zip` desde la carpeta de Drive adjunta en el informe del proyecto.

---
