from flask import Blueprint, render_template, flash, Flask, redirect, url_for
from flask_login import login_required
from __init__ import create_app
import __init__
from flask_sqlalchemy_session import flask_scoped_session
main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html')

@main.route('/index')
def index():
    return render_template('index.html')

@main.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

@main.route('/stream')
def stream():
    return render_template('stream.html')

if __name__ == '__main__':
    db = __init__.db
    app = Flask(__name__)
    app.app_context().push()
    create_app(app)
    db.create_all()
    app.run(debug=True, host='0.0.0.0')