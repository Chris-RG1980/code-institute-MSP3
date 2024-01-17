import sys
from datetime import datetime

from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_login import login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import (
    DateField,
    DecimalField,
    IntegerField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import InputRequired

from muscle_metrics import app, db, login_manager, mongo
from muscle_metrics.models import (
    Exercises,
    MuscleGroups,
    Progress,
    User,
    exercises,
    muscle_groups,
)

from .home import routes
from .login import routes
from .profile import routes
from .register import routes


class ExerciseLogForm(FlaskForm):
    weight = DecimalField(
        "Weight",
        [InputRequired()],
        places=2,
        rounding=None,
        description="Enter weight in kilograms",
    )
    sets = IntegerField(
        "Sets", [InputRequired()], description="Enter the number of sets completed"
    )
    reps = IntegerField(
        "Reps",
        [InputRequired()],
        description="Enter the number of reps per set completed",
    )
    notes = TextAreaField("Notes", render_kw={"placeholder": "Enter your notes here!"})
    submit = SubmitField("Add Exercise")


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


# Logout
@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    flash("You have been logged out!", "success")
    return redirect(url_for("home"))


@app.route("/log", methods=["GET", "POST"])
@login_required
def log():
    form = ExerciseLogForm()

    if form.validate_on_submit():
        print(request.form, file=sys.stderr)

        progress = Progress(
            exercise_id=request.form.get("exercise"),
            weight=form.weight.data,
            reps=form.reps.data,
            sets=form.sets.data,
            notes=form.notes.data,
            date_added=datetime.now(),
        )

        db.session.add(progress)
        db.session.commit()

        flash("Exercise added successfully!", "success")

    muscle_groups = MuscleGroups.query.all()
    exercises = Exercises.query.all()

    return render_template(
        "exercise/exercises.html",
        form=form,
        muscle_groups=muscle_groups,
        exercises=exercises,
    )


@app.route("/get_exercises", methods=["GET"])
@login_required
def get_exercises():
    muscle_group_id = request.args.get("muscle_group_id")
    muscle_group = MuscleGroups.query.get(muscle_group_id)
    return jsonify(muscle_group.exercises)


# Error Pages
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Unauthorised Access
@app.errorhandler(401)
def unauthorised_access(e):
    return render_template("401.html"), 401


# Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
