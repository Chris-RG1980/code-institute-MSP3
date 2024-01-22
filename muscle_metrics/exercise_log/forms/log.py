from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SelectField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, NumberRange


class ExerciseLogForm(FlaskForm):
    # SelectField for choosing a muscle group.
    muscle_group = SelectField(
        "Muscle Group",
        choices=[(0, "Select a muscle group")],
        coerce=int,
        validators=[InputRequired()],
    )

    # SelectField for choosing an exercise.
    exercises = SelectField(
        "Exercises",
        choices=[(0, "Select an exercise")],
        coerce=int,
        validators=[InputRequired()],
    )

    # DecimalField for inputting the weight used in the exercise.
    weight = DecimalField(
        "Weight",
        [InputRequired(), NumberRange(max=1000)],
        places=2,
        rounding=None,
        description="Enter weight in kilograms",
    )

    # IntegerField for the number of sets performed.
    sets = IntegerField(
        "Sets",
        [InputRequired(), NumberRange(min=1, max=30)],
        description="Enter the number of sets completed",
    )

    # IntegerField for the number of repetitions (reps) per set.
    reps = IntegerField(
        "Reps",
        [InputRequired(), NumberRange(min=1, max=30)],
        description="Enter the number of reps per set completed",
    )

    # TextAreaField for additional notes.
    notes = TextAreaField("Notes", render_kw={"placeholder": "Enter your notes here!"})

    # Submit button to submit the form.
    submit = SubmitField("Add Exercise")
