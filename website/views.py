from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_required,current_user
from sqlalchemy.sql.functions import user
from . import db
import json

views=Blueprint("views",__name__)

@views.route("/")
@login_required
def home():
    return render_template("home.html",user=current_user)

@views.errorhandler(401)
def not_found(e):
  return render_template('custom_page.html'), 401

@views.route("/bruh")
def bruh():
  return render_template("bruh.html")