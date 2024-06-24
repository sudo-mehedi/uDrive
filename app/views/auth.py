from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.forms.Forms import RegForm, LoginForm
from app.models import db
from app.models.Users import Users
from app.models.Docs import Folders
import sqlalchemy as sa
from flask_login import login_user, logout_user


auth = Blueprint("auth", __name__)

@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegForm()
    if form.validate_on_submit() and request.method == "POST":
        users = Users(username=form.username.data, email=form.email.data, password=form.password.data)
        try:
            db.session.add_all([users])
            db.session.commit()
            users = Users.query.filter_by(username=form.username.data).first()
            print(users)
            folder = Folders(name='root', user_root=users.username, parent_id=0, created_by=users.id)
            db.session.add(folder)
            db.session.commit()
            flash("Registration Success", category='success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            print(e)
            print("Error")
    return render_template('register.html', form=form)


@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        user = db.session.scalar(
            sa.select(Users).where(Users.username==form.username.data)
        )
        if user != None and form.password.data == user.password:
            login_user(user)
            flash("Login Sucess", category="success")
            return redirect(url_for('drive.index'))
        else:
            flash("Login faild: username/password is wrong", category='danger')
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash("Logout Sucess", category='warning')
    return redirect(url_for('auth.login'))