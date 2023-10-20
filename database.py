import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

baseDir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(baseDir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

#############################################################

class Puppies(db.Model):
      
      id = db.Column(db.Integer, primary_key = True)
      name = db.Column(db.Text)
      age = db.Column(db.Integer)

      def __init__(self, name, age):
            self.name = name
            self.age = age
      
      def __repr__(self):
            return f"Puppy {self.name} is {self.age} year's old"


    
    
