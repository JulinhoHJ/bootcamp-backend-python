# Flask Boilerplate

## Instalación
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

```bash
pip install -r requirements.txt
```

## Migraciones
```bash
flask db init # crea la carpeta migrations - Solo la primera vez
flask db migrate -m "Descripción de la migración" # crea las migraciones
flask db upgrade # actualiza la base de datos
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

