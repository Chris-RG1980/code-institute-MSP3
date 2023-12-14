from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import EqualTo, InputRequired


class ChangePasswordForm(FlaskForm):
    currentPassword = PasswordField("Current Password", [InputRequired()])
    password = PasswordField(
        "Password",
        [
            InputRequired(),
            EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Confirm Password", [InputRequired()])
