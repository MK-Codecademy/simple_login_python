from app import app, db
from forms import SignUpForm
from flask import render_template, redirect, url_for, request
from models import User

#This is the url without any route parameters
@app.route('/')
#This function only returns the index.html page see templates for page details
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST':
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('signed_up'))
    return render_template('signup.html', form=form)

@app.route('/signed_up')
def signed_up():
    return render_template('signed_up.html')