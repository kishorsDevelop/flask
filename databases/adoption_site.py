import os
from forms import AddForm, DeleteForm, AddOwnerForm
from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Migrate(app, db)

### Models ###
class Puppy(db.Model):

    __tablename__ = 'puppies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)  
    owner = db.relationship('Owner', backref = 'puppies', uselist=False)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
       if self.owner:
          return f"Puppy name: {self.name} and has owner: {self.owner.name}."
       else:
          return f"Puppy name: {self.name} has no owner."

class Owner(db.Model):

    __tablename__ = 'owner'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id
    
    def __repr__(self): 
        return f"Owner name is: {self.name}"

### View Functions ###

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/list')
def list():
    names = Puppy.query.all()
    return render_template('list.html', names=names)


@app.route('/add', methods = ['POST', 'GET'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        name = Puppy(name=name)
        db.session.add(name)
        db.session.commit()
        return redirect(url_for('list'))
    
    return render_template('add.html', form=form)

@app.route('/add_owner', methods=['POST', 'GET'])
def add_owner():
    form = AddOwnerForm()
    if form.validate_on_submit():
        name = form.name.data
        puppy_id = form.puppy_id.data
        owner = Owner(name=name, puppy_id=puppy_id)
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for('list'))

    return render_template('add_owner.html', form=form)


@app.route('/delete', methods=['POST', 'GET'])
def delete():
    form = DeleteForm()
    if form.validate_on_submit():
        id = form.id.data
        puppy = Puppy.query.get(id)
        db.session.delete(puppy)
        db.session.commit()
        return redirect(url_for('list'))
    
    return render_template('delete.html', form=form)


if __name__ == '__main__':  
    with app.app_context():
        db.create_all()
    app.run(debug=True)