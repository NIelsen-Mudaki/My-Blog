from flask import (render_template, redirect, url_for,
                    flash, request)
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import SignupForm, LoginForm
from .. import db

@auth.route("/signup", methods = ["GET", "POST"])
def register():
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        user = User(name = signup_form.name.data, 
                    username = signup_form.username.data, 
                    email = signup_form.email.data,
                    password = signup_form.password.data)
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for("auth/login"))
    title = "Sign Up"
    return render_template("auth/signup.html", 
                            signup_form = signup_form,
                            title = title)

@auth.route("/login", methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    user = User.query.filter_by(email = login_form.email.data).first()
    if user:
        flash('user exists')
    else:
        if login_form.validate_on_submit():
            user = User(username=login_form.username.data,
                            email=login_form.email.data)
            db.session.add(user)
            db.session.commit()

            title = "Login"
            return render_template("auth/login.html",
                                    login_form = login_form,
                                        title = title)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))