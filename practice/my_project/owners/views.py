from flask import Flask, Blueprint, render_template, redirect, url_for
from my_project import db
from my_project.models import Owner
from my_project.owners.forms import AddForm

owners_blueprints = Blueprint('owners', __name__, template_folder='templates/owners')

@owners_blueprints.route('/add', methods=['POST', 'GET'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        owner = Owner(name, pup_id)
        db.session.add(owner)
        db.session.commit()
        return redirect(url_for('puppies.list'))
    return render_template('add_owner.html', form=form)
