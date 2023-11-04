from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, ValidationError ,PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from project.models import User

class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired() ,Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password_confirm', message='Password Must Match')])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    
    def validate_email(self, field):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Your email has been already registered')
        
    def validate_username(self, field):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('Username is taken!')
        
