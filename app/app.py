from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required

app = Flask(__name__)

#This key should be a complex string and absolutely should not read 'my_secret_key'
app.config['SECRET_KEY'] = 'my_secret_key'
#What we put as a string at the end here will be what the database will be called
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#variable used to store the instance of SQLAlchemy which is an orm connected to the flask instance
db = SQLAlchemy(app)
#Here we initialise an instance of login manager in the variable login
login = LoginManager()
login.login_view = 'login'







import routes, models