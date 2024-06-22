from flask import Flask
from app.models import db
from flask_migrate import Migrate
from app.views.drive import drive


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///udrive.db"


app.register_blueprint(drive)


def create_app():
    db.init_app(app)

    migrate = Migrate(app, db)

    return app




