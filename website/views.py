# store standard roots in views like login/homepage/subpages etc.
from flask import Blueprint, render_template

# Blueprint means it has a lot of urls inside here 
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")


