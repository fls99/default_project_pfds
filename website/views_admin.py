# store standard roots in views like login/homepage/subpages etc.
from flask import Blueprint, render_template
from flask_login import login_required, current_user

# Blueprint means it has a lot of urls inside here 
views_admin = Blueprint('views_admin', __name__)

@views_admin.route('/admin')
@login_required
def home():
    return render_template("admin/admin_home.html", user=current_user) # here we can reference our current logged user also for template


