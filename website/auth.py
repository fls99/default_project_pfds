from flask import Blueprint

# Blueprint means it has a lot of urls inside here 
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "<h1>Login Page</h1>"