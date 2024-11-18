from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db, ADMIN_CREATION_PASSWORD
from .models import Admin

auth_admin = Blueprint('auth_admin', __name__)


@auth_admin.route('/admin')
def admin_landing():
    return redirect(url_for('auth_admin.admin_login'))

@auth_admin.route('/admin/logout')
@login_required
def admin_logout():
    logout_user()  
    return redirect(url_for('auth_admin.admin_login'))

@auth_admin.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        admin = Admin.query.filter_by(email=email).first()
        if admin and check_password_hash(admin.password, password):
            login_user(admin)
            return redirect(url_for('views_admin.home'))
        else:
            flash('Invalid admin credentials', category='error')
            
    return render_template("admin/admin_login.html", user=current_user)

@auth_admin.route('/admin/sign-up', methods=['GET', 'POST'])
def admin_signup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        admin_level = request.form.get('admin_level', 1)
        creation_password = request.form.get('creation_password')

        admin = Admin.query.filter_by(email=email).first()

        if admin:
            flash('Admin email already exists', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif creation_password != ADMIN_CREATION_PASSWORD:
            flash('Invalid admin creation password', category='error')
        else:
            new_admin = Admin(
                email=email,
                name=name,
                password=generate_password_hash(password1, method='pbkdf2:sha256'),
                admin_level=admin_level
            )
            db.session.add(new_admin)
            db.session.commit()
            flash('Admin account created', category='success')
            return redirect(url_for('auth_admin.admin_login'))

    return render_template("admin/admin_signup.html", user=current_user)