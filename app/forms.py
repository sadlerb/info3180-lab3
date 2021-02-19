from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired,email
class Contactform(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = StringField('E-Mail',validators=[DataRequired(),email()])
    subject = StringField('Subject',validators=[DataRequired()])
    message = TextAreaField('Message',validators=[DataRequired()])

    