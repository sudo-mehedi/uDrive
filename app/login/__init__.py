from flask_login import LoginManager
from app.models import db
from app.models.Users import Users


login_manager = LoginManager()


@login_manager.user_loader
def load_user(id):
    return db.session.get(Users, int(id)) 


login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please login'
login_manager.login_message_category = 'warning'