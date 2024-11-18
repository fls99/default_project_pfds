from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from .models import User, Note
from flask_login import login_user, logout_user, login_required, current_user


# Blueprint means it has a lot of urls inside here 
auth = Blueprint('auth', __name__)

# by default only get requests (when the website hsows us) now also post when we change the state of the website 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form 
    email = data.get('email')
    password = data.get("password")
    user = User.query.filter_by(email=email).first()
    if user:
        user_email = user.email
        if user_email != email:
            flash('Email does not exist.', category='error')
        if check_password_hash(user.password, password):
            flash('Logged in successfully', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
        else:
            flash('Password was incorrect', category='error')
    else:
        flash('Please login to your account', category='success')
        
            
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        # check if user exists and user information matches requirements
        if user:
            flash('Email address already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 1:
            flash('First name must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Verification of password does not match entered password', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters', category='error')
        else:
            new_user = User(email=email, first_name=firstName, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')

            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user=current_user)