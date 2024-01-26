from flask_wtf import FlaskForm

from muscle_metrics.register.forms import RegistrationForm


class EmailForm(FlaskForm):
    """
    A form for updating a user's email address using Flask-WTF.

    This form inherits from FlaskForm and reuses the
    email field from the RegistrationForm defined in the
    muscle_metrics.register.forms module.
    """

    email = RegistrationForm.email
