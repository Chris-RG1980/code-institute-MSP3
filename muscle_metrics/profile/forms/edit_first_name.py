from flask_wtf import FlaskForm

from muscle_metrics.register.forms import RegistrationForm


class FirstNameForm(FlaskForm):
    first_name = RegistrationForm.first_name
