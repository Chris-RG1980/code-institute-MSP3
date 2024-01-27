from flask_wtf import FlaskForm
from wtforms import PasswordField
from wtforms.validators import EqualTo, InputRequired


class ChangePasswordForm(FlaskForm):
    """
    This form includes fields for the current password, a new password,
    and a confirmation field for the new password. It uses validators
    to ensure that the new passwords are entered and match each other.
    """
    currentPassword = PasswordField("Current Password", [InputRequired()])
    password = PasswordField(
        "Password",
        [InputRequired(), EqualTo("confirm", message="Passwords must match")],
    )
    confirm = PasswordField("Confirm Password", [InputRequired()])
