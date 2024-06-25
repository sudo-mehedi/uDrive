from flask import Flask
from flask_migrate import Migrate
from app.views.drive import drive
from app.views.auth import auth
from app.views.dash import dash
from app.models import db
from app.login import login_manager
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///udrive.db"
app.config['SECRET_KEY'] = "This is super secret"
app.config['UPLOAD_FOLDER'] = 'app/uploads'


app.register_blueprint(drive, url_prefix='/d')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(dash)


def create_app():
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app) 
    return app




