from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import Email, InputRequired


class LoginForm(FlaskForm):
    # EmailField for the user's email address.
    email = EmailField(
        "Email Address",
        [
            Email(),
            InputRequired(),
        ],
        render_kw={"placeholder": "email@address.com"},
    )

    # PasswordField for the user's password.
    password = PasswordField(
        "Password",
        [
            InputRequired(),
        ],
    )

    # SubmitField for the submit button.
    submit = SubmitField("")
