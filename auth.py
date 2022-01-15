from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
import models
User = models.User
from flask_login import login_user, logout_user, login_required, current_user
import __init__
db = __init__.db


auth = Blueprint('auth',__name__)
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Email not Found')
        elif not check_password_hash(user.password, password):
            flash('Incorrect Password')
        login_user(user, remember=True)
        return redirect(url_for('social.user'))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='GET':
        return render_template('signup.html')
    else:
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('name')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already in use')
            return redirect(url_for('auth.signup'))
        new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))