from flask import Blueprint

drive = Blueprint("drive", __name__)

@drive.route("/")
def index():
    return "Home"