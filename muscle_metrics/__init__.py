import os

from bson.objectid import ObjectId
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy

if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    Uri = os.environ.get("DATABASE_URL")
if Uri.startswith("postgres://"):
    Uri = Uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = Uri
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

db = SQLAlchemy(app)
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
# Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Routes
from muscle_metrics import routes

with app.app_context():
    db.create_all()
    from . import seed_data
