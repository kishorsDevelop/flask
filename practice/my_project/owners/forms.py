from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField('Enter name of Owner: ')
    pup_id = IntegerField('Enter Id of Puppy: ')
    submit = SubmitField('Add Owner')