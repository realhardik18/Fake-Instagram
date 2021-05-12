from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import login_user,login_required,logout_user,current_user

auth=Blueprint("auth",__name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        return render_template("home.html",user=current_user,boi=email)

    return render_template("login.html")

