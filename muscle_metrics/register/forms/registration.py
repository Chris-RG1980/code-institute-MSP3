from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField, SubmitField
from wtforms.validators import Email, EqualTo, InputRequired, Length


class RegistrationForm(FlaskForm):
    """
    A form for user registration using Flask-WTF.
    """

    # StringField for the user's first name.
    first_name = StringField(
        "First Name",
        [
            InputRequired(),
            Length(max=50),
        ],
        description="Maximum 50 characters",
    )

    # StringField for the user's last name.
    last_name = StringField(
        "Last Name",
        [
            InputRequired(),
            Length(max=50),
        ],
        description="Maximum 50 characters",
    )

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
        [InputRequired(), EqualTo("confirm", message="Passwords must match")],
    )

    # PasswordField for confirming the password.
    confirm = PasswordField("Confirm Password", [InputRequired()])

    # SubmitField for the submit button of the registration form.
    submit = SubmitField("Register")
