from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import Email, InputRequired


class LoginForm(FlaskForm):
    """
    A form for user login using Flask-WTF.

    This form includes three fields: email, password, and submit.
    """
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
