# __init__.py标识这个包

from flask import Flask
from config import Config
from flask_login import LoginManager
import os

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = os.urandom(24)
login = LoginManager(app)

from app import routes
