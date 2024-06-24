from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(add_models_to_shell=True)

from .Users import Users
from .Docs import Folders