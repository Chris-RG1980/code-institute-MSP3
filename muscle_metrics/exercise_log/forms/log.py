from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SelectField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, NumberRange


class ExerciseLogForm(FlaskForm):
    muscle_group = SelectField(
        "Muscle Group",
        choices=[(0, "Select a muscle group")],
        coerce=int,
        validators=[InputRequired()],
    )
    exercises = SelectField(
        "Exercises",
        choices=[
            (
                0,
                "Select an exercise",
            )
        ],
        coerce=int,
        validators=[InputRequired()],
    )
    weight = DecimalField(
        "Weight",
        [InputRequired(), NumberRange(max=1000)],
        places=2,
        rounding=None,
        description="Enter weight in kilograms",
    )
    sets = IntegerField(
        "Sets",
        [InputRequired(), NumberRange(min=1, max=30)],
        description="Enter the number of sets completed",
    )
    reps = IntegerField(
        "Reps",
        [InputRequired(), NumberRange(min=1, max=30)],
        description="Enter the number of reps per set completed",
    )
    notes = TextAreaField("Notes", render_kw={"placeholder": "Enter your notes here!"})
    submit = SubmitField("Add Exercise")
