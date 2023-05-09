from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email

from application.database import db

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=5000)])
    submit = SubmitField('Submit')
