from flask_wtf import FlaskForm

from muscle_metrics.register.forms import RegistrationForm


class LastNameForm(FlaskForm):
    # Change Last Name
    last_name = RegistrationForm.last_name
