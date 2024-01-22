from flask_wtf import FlaskForm

from muscle_metrics.register.forms import RegistrationForm


class EmailForm(FlaskForm):
    # Change email address
    email = RegistrationForm.email
