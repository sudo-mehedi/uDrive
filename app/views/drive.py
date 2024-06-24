from flask import Blueprint, render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from app.models.Docs import Folders
from app.models import db
from flask import current_app
from app.models.Docs import Files

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
        id = folders.id
        subfolders = Folders.query.filter_by(parent_id=folders.id).filter_by(created_by=current_user.id).all()
        files = Files.query.filter_by(parent_id=folders.id).filter_by(created_by=current_user.id)
    else:

        subfolders = Folders.query.filter_by(parent_id=id).filter_by(created_by=current_user.id).all()
        files = Files.query.filter_by(parent_id=id).filter_by(created_by=current_user.id)

    path = Folders.get_path_with_ids(id)
    return render_template('home.html', subfolders=subfolders, id=id, paths=path, files=files)


@drive.route('/create_folder', methods=["POST"])
@login_required
def create_folder():
    parent_id = request.form['parent_id']
    if(len(Folders.query.filter_by(id=parent_id).filter_by(created_by=current_user.id).all())) !=0:
        new_folder = Folders(name=request.form['name'],
                            parent_id=request.form['parent_id'], 
                            created_by=current_user.id)
        db.session.add(new_folder) 
        db.session.commit()
        return redirect(url_for('drive.index', id=parent_id))
    else:
        return abort(404)


from werkzeug.utils import secure_filename
import os

@drive.route('/upload_file', methods=['POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("Please select files", category='danger')
        file = request.files['file']
        if file.filename == '':
            flash('Please Select a file', category="danger")
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
            new_file = Files(parent_id=request.form['parent_id'], 
                            name=filename, 
                            path=os.path.join(current_app.config['UPLOAD_FOLDER'], filename),
                            created_by=current_user.id
                        ) 
            db.session.add(new_file)
            db.session.commit()
            flash("File upload sucessful", category="success")
        
    return redirect(url_for('drive.index', id=request.form['parent_id']))