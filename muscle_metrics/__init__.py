import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


def import_routes():
    """
    Import the 'routes' module from the 'muscle_metrics' package.
    """
    from muscle_metrics import routes


import_routes()

with app.app_context():
    db.create_all()
    from . import seed_data
