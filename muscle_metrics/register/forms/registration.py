from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo


# Create registration form
class RegistrationForm(FlaskForm):
    first_name = StringField(
        "First Name",
        [
            InputRequired(),
            Length(max=50),
        ],
        description="Maximum 50 characters",
    )

    last_name = StringField(
        "Last Name",
        [
            InputRequired(),
            Length(
                max=50,
            ),
        ],
        description="Maximum 50 characters",
    )
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
            EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Confirm Password", [InputRequired()])
    submit = SubmitField("Register")
