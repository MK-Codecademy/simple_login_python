from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login = LoginManager()
login.login_view = 'login'







import routes, models