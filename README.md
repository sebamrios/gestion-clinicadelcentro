# 🏥 Gestión Clínica del Centro

Sistema web de gestión integral para la **Clínica del Centro**, desarrollado con **Django 5.2.5**. Permite administrar profesionales, pacientes, turnos, secretarias, alquileres de consultorios y consultas de contacto.

---

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Módulos](#-módulos)
- [Despliegue](#-despliegue)
- [Licencia](#-licencia)

---

## ✨ Características

- **Gestión de Profesionales**: Alta, baja, edición y búsqueda de profesionales médicos con especialidades, patologías, obras sociales y horarios.
- **Gestión de Pacientes**: Registro y administración de pacientes con datos personales, documento y obra social.
- **Sistema de Turnos**: Creación de agendas por profesional, asignación de turnos con estados (Pendiente, Confirmado, Cancelado, Realizado), vista de calendario y auditoría de cambios.
- **Gestión de Secretarias**: Perfil de secretarias vinculado a usuarios del sistema, con control de licencias (vacaciones, médicas, permisos especiales) y tramos de licencia.
- **Alquileres**: Módulo para la gestión de alquileres de consultorios.
- **Contacto**: Formulario público de consultas con seguimiento de estado (Sin Contestar, En Proceso, Contestada) y sistema de respuestas.
- **Usuarios**: Registro, login, perfil con imagen y datos personales completos.
- **Captcha**: Protección de formularios con `django-simple-captcha`.

---

## 🛠 Tecnologías

| Componente     | Tecnología                          |
|----------------|-------------------------------------|
| Backend        | Python / Django 5.2.5               |
| Base de Datos  | SQLite3                             |
| Frontend       | Django Templates + HTML/CSS         |
| Captcha        | django-simple-captcha 0.6.2         |
| Imágenes       | Pillow 11.3.0                       |
| Hosting        | PythonAnywhere                      |
| Zona Horaria   | America/Argentina/Buenos_Aires      |
| Idioma         | Español (Argentina)                 |

---

## 📌 Requisitos Previos

- **Python 3.10+**
- **pip** (gestor de paquetes de Python)
- **Git** (opcional, para clonar el repositorio)

---

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/sebamrios/gestion-clinicadelcentro.git
cd gestion-clinicadelcentro
```

### 2. Crear y activar un entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear un superusuario

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Acceder a la aplicación en: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Panel de administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📁 Estructura del Proyecto

```
gestion-clinicadelcentro/
├── clinica/                 # Configuración principal de Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── myApps/                  # Aplicaciones del proyecto
│   ├── profesionales/       # Gestión de profesionales y especialidades
│   ├── pacientes/           # Gestión de pacientes
│   ├── turnos/              # Agendas y turnos médicos
│   ├── secretarias/         # Secretarias y licencias
│   ├── alquileres/          # Alquileres de consultorios
│   ├── contacto/            # Consultas y respuestas
│   └── usuarios/            # Registro, login y perfiles
├── templates/               # Plantillas HTML globales
│   ├── base.html
│   ├── clinica/
│   ├── profesionales/
│   ├── pacientes/
│   ├── turnos/
│   ├── alquileres/
│   ├── contacto/
│   └── usuarios/
├── static_dev/              # Archivos estáticos de desarrollo (CSS, JS, imágenes)
├── manage.py
├── requirements.txt
└── README.md
```

---

## 📦 Módulos

### 🩺 Profesionales (`myApps/profesionales`)

- **Modelos**: `Especialidad`, `Profesional`
- **Funcionalidades**: Listado, creación, edición, detalle, búsqueda y filtrado de profesionales por especialidad.
- **Vistas**: Home de la clínica, lista, crear, editar, detalle, buscar, filtrar.

### 👤 Pacientes (`myApps/pacientes`)

- **Modelo**: `Paciente` (nombre, apellido, documento único, fecha de nacimiento, teléfono, obra social)
- **Funcionalidades**: CRUD completo con confirmación de eliminación.

### 📅 Turnos (`myApps/turnos`)

- **Modelos**: `Agenda`, `Turno`
- **Funcionalidades**:
  - Cada profesional tiene una agenda única.
  - Secretarias asignadas a agendas.
  - Turnos con estados: Pendiente, Confirmado, Cancelado, Realizado.
  - Auditoría: registro de quién creó y modificó cada turno.
  - Restricción de unicidad: un solo turno por agenda y horario.
  - Vista de calendario y edición de turnos.

### 🗂 Secretarias (`myApps/secretarias`)

- **Modelos**: `Secretaria`, `Licencia`, `TramoLicencia`
- **Funcionalidades**:
  - Perfil vinculado al usuario del sistema.
  - Gestión de licencias por tipo (Vacaciones, Médica, Permiso Especial, Otra).
  - Tramos de licencia con cálculo automático de días tomados y pendientes.
  - Asignación de suplente.

### 🏢 Alquileres (`myApps/alquileres`)

- Gestión de alquileres de consultorios con listado.

### 📩 Contacto (`myApps/contacto`)

- **Modelos**: `Consulta`, `Respuesta`
- **Funcionalidades**:
  - Formulario de contacto público con captcha.
  - Seguimiento de estado de consultas.
  - Sistema de respuestas que actualiza automáticamente el estado a "Contestada".

### 👥 Usuarios (`myApps/usuarios`)

- **Modelo**: `Usuario` (perfil extendido con imagen, datos personales, ubicación, documentos)
- **Funcionalidades**: Registro, login, perfil de usuario.

---

## 🌐 Despliegue

El proyecto está configurado para desplegarse en **PythonAnywhere**:

- **Dominio**: `clinicadelcentro.pythonanywhere.com`
- Archivos estáticos servidos desde `staticfiles/` (generados con `python manage.py collectstatic`).
- Archivos multimedia servidos desde `media/`.

---

## 📄 Licencia

Este proyecto es de uso privado para la **Clínica del Centro**.
