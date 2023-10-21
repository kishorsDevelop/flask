import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Migrate(app, db)

class Puppy(db.Model):

    __tablename__ = 'puppies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)  

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"Puppy name is {self.name}"
    



