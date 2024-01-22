from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import EqualTo, InputRequired


class ChangePasswordForm(FlaskForm):
    # PasswordField for the current password.
    currentPassword = PasswordField("Current Password", [InputRequired()])

    # PasswordField for the new password.
    password = PasswordField(
        "Password",
        [InputRequired(), EqualTo("confirm", message="Passwords must match")],
    )

    # PasswordField for confirming the new password.
    confirm = PasswordField("Confirm Password", [InputRequired()])
