from flask import Blueprint, render_template

dash = Blueprint('dash', __name__)

@dash.route('/')
def index():
    return render_template('dash.html')


@dash.route('/about')
def about():
    return "This is about page"