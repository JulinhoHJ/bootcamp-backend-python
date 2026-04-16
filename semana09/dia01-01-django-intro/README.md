Nota: tener instalado Python 3.x.y
1. Instalar el entorno virtual de Python
# python -m venv entorno_django
# entorno_django/bin/activate -> windows
# source entorno_django/bin/activate -> linux
2. Instalar Django 3.2.x
# pip install django
3. Crear un nuevo proyecto
# django-admin startproject proyecto .
4. Ejecutar el servidor de desarrollo
# python manage.py runserver
5. Acceder a la pagina de inicio de Django
# http://127.0.0.1:8000/
6. Realizar una migración
# python manage.py migrate
7. Crear un usuario (admin, admin@gmail.com, adminadmin)
# python manage.py createsuperuser
8. Acceder a la pagina de inicio de Django
# http://127.0.0.1:8000/admin/

# Introducción a Django

## Instalación

```bash
python -m venv entorno_django
source entorno_django/Scripts/activate
pip install django
```

## Creación del proyecto

```bash
django-admin startproject django_intro .
```

## Inicio del servidor

```bash
python manage.py runserver
```

## Migraciones

```bash
# Crear los documentos de migraciones
python manage.py makemigrations

# Ejecutar las migraciones
python manage.py migrate

# Listar las migraciones
python manage.py showmigrations
```

## Creación de usuario

```bash
python manage.py createsuperuser
```

## Creación de aplicación

```bash
python manage.py startapp almacen
```