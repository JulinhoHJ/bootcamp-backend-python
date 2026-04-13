# Flask Boilerplate

Este es un boilerplate de flask con algunas dependencias y configuraciones que se pueden usar para comenzar a desarrollar una aplicación Flask.

## Tecnologías y Requisitos
* **Python**: >= 3.12.x
* **framework**: Flask 3.x
* **Base de datos**: PostgreSQL
* **Gestión de entorno**: venv

## Instalación y Configuración

1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/user/repo.git
    ```
2. **Crear y activar el entorno virtual:**
    ```bash
    python -m venv venv
    # En Linux/macOS
    source venv/bin/activate
    # En Windows
    venv\Scripts\activate
    ```
3. **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Variables de entorno:** `.env`
    ```bash
    DATABASE_URI = ''
    JWT_SECRET_KEY = ''
    ```
## Migraciones
```bash
flask db init # crea la carpeta migrations - Solo la primera vez
flask db migrate -m "Descripción de la migración" # crea las migraciones
flask db upgrade # actualiza la base de datos
```
## Ejecución
```bash
python run.py
```
## Estructura del proyecto
```bash
├── app
│   ├── models
│   │   ├── user_model.py
│   │   └── role_model.py
│   ├── resources
│   │   ├── auth_resource.py
│   │   ├── user_resource.py
│   │   └── role_resource.py
│   ├── schemas
│   │   ├── auth_schema.py
│   │   ├── user_schema.py
│   │   └── role_schema.py
│   ├── services
│   │   ├── user_service.py
│   │   └── role_service.py
│   ├── __init__.py
│   └── routes.py
├── migrations
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   ├── alembic.ini
│   └── versions
├── README.md
├── requirements.txt
├── run.py
├── .gitignore
├── config.py
└── db.py

```
## Testing
```bash
pytest
```
## Despliegue

