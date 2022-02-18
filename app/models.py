from datetime import datetime
from flask_login import UserMixin
from app import db, login_manager
from werkzeug.security import (generate_password_hash,
                               check_password_hash)

@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique = True)
    email = db.Column(db.String(255), unique = True, index = True)
    avatar_path = db.Column(db.String(255))
    password = db.Column(db.String(255))
    posts = db.relationship("Post", backref = "user", lazy = "dynamic")

    def verify_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def get_user_posts(cls,id):
        posts = Post.query.filter_by(user_id = id).order_by(Post.posted_at.desc()).all()
        return posts

    @classmethod
    def get_all_posts(cls):
        return Post.query.order_by(Post.posted_at).all()



class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    post_title = db.Column(db.String)
    post_content = db.Column(db.Text)
    posted_at = db.Column(db.DateTime)
    post_by = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))




class Quote:
    """
    Blueprint class for quotes consumed from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote