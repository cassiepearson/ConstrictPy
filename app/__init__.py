from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from constrictpy.logger import getLogger

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)

from app import routes
