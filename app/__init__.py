from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__) # default flask naming convention
app.config.from_object(Config) # standard (i think) config for a flask app
db = SQLAlchemy(app) # database form flask-sqlalchemy
migrate = Migrate(app, db) # handles database migrations/updates
login = LoginManager(app) # login manager from flask_login handles logins 
login.login_view = 'login' # login_view provides user auth to specified pages
from app import routes, models