# Flask ticket

Este es una app de gestión de tickets donde una empresa con múltiples sedes puede registrar, asignar, atender y cerrar tickets de incidencias que se generan en distintas sedes.

Cada ticket es generado por un solicitante y se clasifica por categoría y área dentro de una sede específica. Los usuarios, pertenecientes a distintas sedes y con roles definidos, son responsables de atender estos tickets siguiendo un flujo estructurado: asignación, atención y cierre. El sistema permite controlar el estado del ticket, registrar fechas clave del proceso y almacenar la solución brindada.

## Tecnologías y Requisitos
* **Python**: >= 3.12.x
* **framework**: Flask 3.x
* **Base de datos**: PostgreSQL
* **Gestión de entorno**: venv

## Instalación y Configuración

1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/JulinhoHJ/bootcamp-backend-python/tree/main/semana08/py-flask-ticket
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
## Testing
```bash
pytest
```
## Despliegue

