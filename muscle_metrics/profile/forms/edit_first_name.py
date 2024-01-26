from flask_wtf import FlaskForm

from muscle_metrics.register.forms import RegistrationForm


class FirstNameForm(FlaskForm):
    """
    A form for updating a user's first name using Flask-WTF.

    This form inherits from FlaskForm and utilizes the first_name
    field from the RegistrationForm defined in the
    muscle_metrics.register.forms module.
    """

    first_name = RegistrationForm.first_name
