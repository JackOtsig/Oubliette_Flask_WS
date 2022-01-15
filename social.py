from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
import __init__
db = __init__.db
social = Blueprint('social', __name__)


@social.route('/user')
@login_required
def user():
    from flask_login import current_user
    username = current_user.name
    return redirect(url_for('social.users', username=username))

@social.route('/users/<username>')
@login_required
def users(username):
    from flask_login import current_user
    username = current_user.name
    posts = [
        {'author': username, 'body': 'Test post #1'}
    ]
    return render_template('user.html', user=username, posts=posts)

@social.route('/search')
def search():
    return render_template('search.html')