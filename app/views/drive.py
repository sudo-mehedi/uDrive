from flask import Blueprint, render_template, request, redirect, url_for, abort, flash, Response
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
        
        subfolders = Folders.query.filter_by(parent_id=folders.id).filter_by(created_by=current_user.id)
        files = Files.query.filter_by(parent_id=folders.id).filter_by(created_by=current_user.id)
    else:

        subfolders = Folders.query.filter_by(parent_id=id).filter_by(created_by=current_user.id)
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
        flash("Folder created", category="success")
        return redirect(url_for('drive.index', id=parent_id))
    else:
        return abort(404)


from werkzeug.utils import secure_filename
from app.utils.file_name import unique_name
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
            ufilename = unique_name(filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], ufilename))
            new_file = Files(parent_id=request.form['parent_id'], 
                            name=filename, 
                            path=ufilename,
                            created_by=current_user.id
                        ) 
            db.session.add(new_file)
            db.session.commit()
            flash("File upload sucessful", category="success")
        
    return redirect(url_for('drive.index', id=request.form['parent_id']))


from flask import send_from_directory

@drive.route('/<id>/download')
@login_required
def download(id=None):
    if id == None:
        return abort(404)
    
    file = Files.query.filter_by(created_by=current_user.id).filter_by(id=id).first()
    if file is None or file is []:
        return abort(404)
    return send_from_directory('./uploads', file.path, as_attachment=True)




@drive.route("/delete", methods=["POST"])
@login_required
def delete_files_folders():
    _type = request.form.get('type')
    _id = request.form.get('id')
    print(_type, _id)
    if _type == 'folder':
        do = Folders.query.filter_by(created_by=current_user.id).filter_by(id=_id).first()
        db.session.delete(do)
        db.session.commit()
    elif _type == 'file':
        do = Files.query.filter_by(created_by=current_user.id).filter_by(id=_id).first()
        db.session.delete(do)
        db.session.commit()
    return Response("", headers={"HX-Refresh": "true"})