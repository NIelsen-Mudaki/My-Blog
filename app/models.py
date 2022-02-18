from datetime import datetime
from flask_login import UserMixin
from app import db, login_manager

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
    password_hash = db.Column(db.String(255))
    posts = db.relationship("Post", backref = "user", lazy = "dynamic")


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