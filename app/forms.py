from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignUpForm(FlaskForm):
    username = StringField(("Username"), validators=[DataRequired(), Length(max=20)])
    email = EmailField(("Email"), validators=[Email(), DataRequired(), Length(max=64)])
    password = PasswordField(("Password"), validators=[DataRequired(), Length(min=6, message="Minimum password length is 6 characters")])
    repeat_password = PasswordField(("Repeat Password"), validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign Up")