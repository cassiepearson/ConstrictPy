from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from constrictpy.io_handling import ensureDir
from redis import Redis
import rq

app = Flask(__name__)
Bootstrap(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.redis = Redis.from_url(app.config["REDIS_URL"])
app.task_queue = rq.Queue("app-tasks", connection=app.redis)

ensureDir(app.config.get("UPLOAD_FOLDER"))
ensureDir(app.config.get("RESULTS_FOLDER"))

from app import routes, models
