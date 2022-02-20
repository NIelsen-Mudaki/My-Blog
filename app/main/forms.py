from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField,
                    SubmitField)
from wtforms.validators import InputRequired

class PostForm(FlaskForm):
    title = StringField("Blog title:", validators=[InputRequired()])
    post = TextAreaField("Type Away:", validators=[InputRequired()])
    submit = SubmitField("Post")

class CommentForm(FlaskForm):
    comment = TextAreaField("Post Comment", validators=[InputRequired()])
    alias = StringField("Comment by:")
    submit = SubmitField("Comment")