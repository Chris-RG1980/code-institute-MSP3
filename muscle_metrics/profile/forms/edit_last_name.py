from flask_wtf import FlaskForm

from muscle_metrics.register.forms import RegistrationForm


class LastNameForm(FlaskForm):
    """
    A form for updating a user's last name using Flask-WTF.

    This form inherits from FlaskForm and uses the last_name
    field from the RegistrationForm defined in the
    muscle_metrics.register.forms module.
    """

    last_name = RegistrationForm.last_name
