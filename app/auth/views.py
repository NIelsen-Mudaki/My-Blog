from flask import (render_template, redirect, url_for,
                    flash, request)
from flask_login import login_user, logout_user, login_required
from . import auth
from app.models import User
from app.auth.forms import SignupForm, LoginForm
from .. import db

@auth.route("/signup", methods = ["GET", "POST"])
def signup():
    signup_form = SignupForm()
    if signup_form.validate_on_submit():
        password = signup_form.password.data
        user = User(name = signup_form.name.data, 
                    username = signup_form.username.data, 
                    email = signup_form.email.data)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()
        flash('Account created successfully')
        
        return redirect(url_for('auth.login'))
    title = " My Blog | Get a chance to express yourself"
    return render_template("auth/signup.html", 
                            signup_form = signup_form,
                            title = title)

@auth.route("/login", methods = ["GET", "POST"])
def login():
    login_form = LoginForm()
    user = User.query.filter_by(email = login_form.email.data).first()
    if user is not None and user.verify_password(login_form.password.data):
        login_user(user)
        return redirect(url_for("main.index"))
    

    title = " My Blog | Get a chance to express yourself"
    return render_template("auth/login.html",login_form = login_form,title = title)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))