from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from constrictpy.io_handling import ensureDir

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

ensureDir(app.config.get("UPLOAD_FOLDER"))
ensureDir(app.config.get("RESULTS_FOLDER"))

from app import routes, models
