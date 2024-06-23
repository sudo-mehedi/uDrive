from flask import Blueprint, render_template
from flask_login import login_required, current_user
drive = Blueprint("drive", __name__)

@drive.route("/")
@login_required
def index():
    return render_template('base.html')