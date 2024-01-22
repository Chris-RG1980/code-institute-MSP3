from flask_wtf import FlaskForm

from muscle_metrics.register.forms import RegistrationForm


class FirstNameForm(FlaskForm):
    # Change First Name
    first_name = RegistrationForm.first_name
