from app.auth.forms import LoginForm
from .. import db
from . import main
from ..requests import get_quote
from ..models import User, Post, Comment
from .forms import PostForm,CommentForm
from flask import flash, render_template, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime



@main.route("/", methods = ["GET", "POST"])
def index():
    quote = get_quote()



    return render_template("index.html", quote = quote)

@main.route("/new-post", methods = ["POST", "GET"])
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

    return render_template("new-post.html",
                            post_form = post_form)


@main.route("/posts", methods = ["POST", "GET"])
@login_required
def post():
    posts = Post.query.all()
    user = current_user

    display_posts = posts

    return render_template('posts.html', posts=posts, user=user, display_posts=display_posts)
