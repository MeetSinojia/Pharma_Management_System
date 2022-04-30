from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = "ae78979847432e2d0361f173db4d3573"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home'
login_manager.login_message = 'Only admin can access this!!'
login_manager.login_message_category = 'info'
db = SQLAlchemy(app)

from pharmaton import routes
