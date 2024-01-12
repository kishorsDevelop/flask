import os
from flask import Flask, render_template, redirect, url_for
from forms import AddForm, DelForm, AddOwner
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = 'abc'

### SQL DATABASE ###

baseDir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Owner(db.Model):
    __tablename__ = 'owner'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    pup_id = db.Column(db.Integer, db.ForeignKey('puppy.id'))
    
    def __init__(self, name, id):
        self.name = name
        self.pup_id = id
    
    def __repr__(self):
        return f"Owner Name: {self.name}"

class Puppy(db.Model):
    __tablename__ = 'puppy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner', backref='Puppy', uselist=False)

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        return f"Puppy name: {self.name} and now owner assigned yet!"

#### VIEW FUNCTIONS ####
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['POST', 'GET'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)

@app.route('/list', methods=['POST', 'GET'])
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['POST', 'GET'])
def del_pup():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('delete.html', form=form)

@app.route('/add_owner', methods=['POST', 'GET'])
def add_owner():
    form = AddOwner()
    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        owner = Owner(name, pup_id)
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add_owner.html', form=form)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)