# Configuración de Git

## Usar Git Bash en el terminal

# Configuración incial

## git config --global user.name "Julinho HJ"
## git config --global user.email "wjulinho.hj@gmail.com"

# Iniciar Git

## git init (en el directorio que queremos iniciar el repositorio)
## git status
## git add .
## git commit -m "Mensaje"

# Conectar con GitHub

## git remote add origin https://github.com/JulinhoHJ/bootcamp-backend-python.git (reemplar con el link del repositorio)
## git remote -v (verificar que se ha conectado con el repositorio)

# Subir proyecto a GitHub

## git branch -M main (crear una rama llamada main)
## git push -u origin main (subir la rama main al repositorio)

# Flujo de trabajo

## git add .
## git commit -m "Descripción del cambio"
## git push

### Otros (Anotaciones)
```bash
pip install Flask
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-restful
pip install pydantic
pip install psycopg2-binary
pip install flask-cors
pip install flask-jwt-extended
pip install python-dotenv
pip install flask-migrate
pip install bcrypt
```
## Listar dependencias
```bash
pip freeze > requirements.txt
```

# RUTA
## Configurar models -> modelamos las tablas
## Configurar services -> insertamos los datos y extraemos información (CRUD y otros)
## Configurar resources -> configuramos la logica
## Configurar las rutas -> configuramos la ruta

## Storage
pip install cloudinary

## CORS -> para que el front-end pueda acceder a la api
pip install flask-cors

## ISO STRING -> para formatear fechas