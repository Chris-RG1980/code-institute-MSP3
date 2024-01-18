from datetime import datetime

from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from muscle_metrics import app, db
from muscle_metrics.models import Exercises, MuscleGroups, Progress

from .forms import ExerciseLogForm


@app.route("/log", methods=["GET", "POST"])
@login_required
def log():
    form = ExerciseLogForm()

    muscle_groups = MuscleGroups.query.all()
    form.muscle_group.choices = [(0, "Select a muscle group")] + [
        (mg.id, mg.name) for mg in muscle_groups
    ]

    if request.method == "POST":
        selected_muscle_group = request.form.get("muscle_group")
        exercises = Exercises.query.filter_by(
            muscle_group_id=selected_muscle_group
        ).all()
        form.exercises.choices = [(0, "Select an exercise")] + [
            (ex.id, ex.name) for ex in exercises
        ]

    if form.validate_on_submit():
        progress = Progress(
            user_id=current_user.id,
            muscle_group_id=form.muscle_group.data,
            exercise_id=form.exercises.data,
            weight=form.weight.data,
            reps=form.reps.data,
            sets=form.sets.data,
            notes=form.notes.data,
            date_added=datetime.now(),
        )

        db.session.add(progress)
        db.session.commit()

        flash("Exercise added successfully!", "success")
        return redirect(url_for("log"))

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
