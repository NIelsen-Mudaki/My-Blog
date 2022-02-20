from app.auth.forms import LoginForm
from .. import db
from . import main
from ..requests import get_quote
from ..models import User, Post, Comment
from .forms import PostForm,CommentForm
from flask import render_template, redirect, url_for
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


@main.route("/posts/<int:id>", methods = ["POST", "GET"])
@login_required
def post(id):
    post = Post.query.filter_by(id = id).first()
    comments = Comment.query.filter_by(post_id = id).all()
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
        comment_form.comment.data = ""
        comment_alias = comment_form.alias.data
        comment_form.alias.data = ""
        if current_user.is_authenticated:
            comment_alias = current_user.username
        new_comment = Comment(comment = comment, 
                            comment_at = datetime.now(),
                            comment_by = comment_alias,
                            post_id = id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for("main.post", id = post.id))

    return render_template("posts.html",
                            post = post,
                            comments = comments,
                            comment_form = comment_form)
