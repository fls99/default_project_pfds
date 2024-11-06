from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash

# Blueprint means it has a lot of urls inside here 
auth = Blueprint('auth', __name__)

# by default only get requests (when the website hsows us) now also post when we change the state of the website 
@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form #immutable multi dict only when post 
    print(data)
    return render_template("login.html", text=True)

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters', category='error')
        elif len(firstName) < 4:
            flash('First name must be greater than 4 characters', category='error')
        elif password1 != password2:
            flash('Verification of password does not match entered password', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters', category='error')
        else:
            flash('Account created', category='success')
            new_user = User(email=email, firstName=firstName, password=generate_password_hash(password1))
            db.Session.add(new_user)
            db.Session.commit()
            flash('Account created!', category='success')

            return redirect(url_for('views.home'))

            # add user to data base 
            pass
    return render_template("sign_up.html")