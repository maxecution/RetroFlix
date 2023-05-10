from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired, Length, Email 

from application.database import db

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=5000)])
    submit = SubmitField('Submit')

class HelpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    ticket_type = SelectField('Choose One..', choices=[('Technical', 'Technical'), ('Account', 'Account'), ('Orders', 'Orders'), ('Payment', 'Payment'), ('Returns', 'Returns')])
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=5000)])
    submit = SubmitField('Submit')

class CareersForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=255)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    job_title = StringField('Job Title', validators=[DataRequired(), Length(max=255)])
    location = StringField('Location', validators=[DataRequired(), Length(max=255)])
    expertise = SelectField('Expertise', choices=[('Technical', 'Technical'), ('Marketing', 'Marketing'), ('Sales', 'Sales'), ('Finance', 'Finance'), ('Corporate', 'Corporate'), ('Other', 'Other')])
    cv = FileField('Document', validators=[FileRequired(), FileAllowed(['pdf', 'doc', 'docx', 'odt'], 'Text Document only!')])
    submit = SubmitField('Submit')