from flask import Blueprint, render_template

# Blueprint means it has a lot of urls inside here 
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")