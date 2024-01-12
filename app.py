"""
Jinja Template engines allow us to pass the data from the server-side to 
HTML pages whenever the user makes the request.
"""
from project import app, db
from flask import render_template, Flask, flash, url_for, redirect, request
from flask_login import login_user, login_required, logout_user
from project.models import User
from project.forms import LoginForm, RegistrationForm

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are logged out!")
    return redirect(url_for('home'))

@app.route('login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            flash("Logged in Successfully!")
            next = request.args.get('next')
            if next is None or not next[0] == '/':
                next = url_for('welcome_user')
            return redirect(next)
    return render_template('login.html', form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        username = form.username.data
        password = form.password.data
        user = User(email=email, username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for Registration!")
        return redirect(url_for('login'))
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)


