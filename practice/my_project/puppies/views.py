from flask import Flask, Blueprint, render_template, redirect, url_for
from my_project import db
from my_project.models import Puppy
from my_project.puppies.forms import AddForm, DelForm

puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')

@puppies_blueprint.route('/add', methods=['POST', 'GET'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('add.html', form=form)

@puppies_blueprint.route('/list', methods=['POST', 'GET'])
def list():
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@puppies_blueprint.route('/delete', methods=['POST', 'GET'])
def delete():
    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('delete.html', form=form)
