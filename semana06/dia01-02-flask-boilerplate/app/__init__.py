from flask import Flask
from config import Config
from flask_migrate import Migrate # type: ignore
from flask_jwt_extended import JWTManager # type: ignore
from db import db
from app.models import role_model, user_model

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from app import routes