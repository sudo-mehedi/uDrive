from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models.Docs import Folders
from app.models import db

drive = Blueprint("drive", __name__)


# def create_folder(name, parent_id):
#     new_folder = Folders(name=name, parent_id=parent_id)
#     db.session.add(new_folder)
#     db.session.commit()
    


@drive.route("/", methods=["GET", "POST"])
@drive.route("/<id>/", methods=["GET", "POST"])
@login_required
def index(id=None):
    parent_id = id
    if(id == None):
        username = current_user.username
        folders = Folders.query.filter_by(user_root=username).first_or_404()
        parent_id = folders.id
        subfolders = Folders.query.filter_by(parent_id=folders.id)
        
    else:
        subfolders = Folders.query.filter_by(parent_id=id)
        path = Folders.get_path_with_ids(id)
    return render_template('home.html', subfolders=subfolders, id=id, paths=path)


@drive.route('/create_folder', methods=["POST"])
def create_folder():
    print(request.form['name'])
    new_folder = Folders(name=request.form['name'], parent_id=request.form['parent_id'])
    db.session.add(new_folder)
    db.session.commit()
    return redirect(url_for('drive.index', id=request.form['parent_id']))