import os
from Flask import flask, url_for, redirect
from flask_sqlalchemy import Sqlalchemy
from flask_migrate import Migrate
from flask_login import LoginManager

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

login_manager = LoginManager()

app.config['SECRET_KEY'] = 'my_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(base_dir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = Sqlalchemy(app)
Migrate(app, db)

login_manager.init_app(app)
login_manager.login_view = 'login'





if __name__ == '__main__':
    app.run(debug=True)

