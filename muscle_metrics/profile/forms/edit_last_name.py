from flask_wtf import FlaskForm

from muscle_metrics.register.forms import RegistrationForm


class LastNameForm(FlaskForm):
    last_name = RegistrationForm.last_name
