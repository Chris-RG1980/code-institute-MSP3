from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import Email, InputRequired


# Create login form
class LoginForm(FlaskForm):
    email = EmailField(
        "Email Address",
        [
            Email(),
            InputRequired(),
        ],
        render_kw={"placeholder": "email@address.com"},
    )
    password = PasswordField(
        "Password",
        [
            InputRequired(),
        ],
    )
    submit = SubmitField("")
