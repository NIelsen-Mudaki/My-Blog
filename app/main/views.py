from app.auth.forms import LoginForm
from .. import db
from . import main
from ..requests import get_quote
from ..models import User, Post
from .forms import PostForm
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime



@main.route("/", methods = ["GET", "POST"])
def index():
    quote = get_quote()



    return render_template("index.html", quote = quote)

@main.route("/new_post", methods = ["POST", "GET"])
@login_required
def new_post():
    post_form = PostForm()
    if post_form.validate_on_submit():
        post_title = post_form.title.data
        post_form.title.data = ""
        post_content = post_form.post.data
        post_form.post.data = ""
        new_post = Post(post_title = post_title,
                        post_content = post_content,
                        posted_at = datetime.now(),
                        post_by = current_user.username,
                        user_id = current_user.id)
        db.session.add(new_post)
        db.session.commit()

    
    return render_template("new_post.html",
                            post_form = post_form)
