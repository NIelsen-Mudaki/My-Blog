from .. import db
from . import main
from ..requests import get_quote
from ..models import User, Post
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user



@main.route("/", methods = ["GET", "POST"])
def index():
    quote = get_quote()


    return render_template("index.html", quote = quote)
