import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # CSRF token generation
    SECRET_KEY = os.environ.get("SECRET_KEY") or "alsdfjklasdklfj"

    # flask-sqlalchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis
    REDIS_URL = os.environ.get("REDIS_URL") or "redis://"

    # Directories
    UPLOAD_FOLDER = "app/uploads"
    RESULTS_FOLDER = "app/results"
