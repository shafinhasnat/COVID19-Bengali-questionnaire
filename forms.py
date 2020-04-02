from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length, Email
class Answer(FlaskForm):
	submit = SubmitField('সাবমিট')