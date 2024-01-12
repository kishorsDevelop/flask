from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
    name = StringField("Name of Puppy: ")
    submit = SubmitField("Add Puppy")

class DelForm(FlaskForm):
    id = IntegerField("Id Number of Puppy to be removed: ")
    submit = SubmitField("Remove Puppy")
  
class AddOwner(FlaskForm):
    name = StringField('Enter name of Owner: ')
    pup_id = IntegerField('Enter Id of Puppy: ')
    submit = SubmitField('Add Owner')