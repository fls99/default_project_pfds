# store standard roots in views like login/homepage/subpages etc.
from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Blueprint means it has a lot of urls inside here 
views = Blueprint('views', __name__, template_folder='templates')

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user) # here we can reference our current logged user also for template


