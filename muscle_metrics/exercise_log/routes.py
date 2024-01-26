from datetime import datetime

import flask
from flask import flash, jsonify, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from muscle_metrics import app, db
from muscle_metrics.models import Exercises, MuscleGroups, Progress

from .forms import ExerciseLogForm


@app.route("/log", methods=["GET", "POST"])
@login_required
def log():
    """
    Handle the logging of exercises.

    This route allows authenticated users to log their exercises.
    It handles both the display of the exercise log form and the
    submission of new exercise logs.

    Returns:
    Template or Redirection: Renders the exercise log form template or
    redirects to the log page after successful submission.
    """
    try:
        form = ExerciseLogForm()

        muscle_groups = MuscleGroups.query.all()
        form.muscle_group.choices = [(0, "Select a muscle group")] + [
            (mg.id, mg.name) for mg in muscle_groups
        ]

        if request.method == "POST":
            exercises = Exercises.query.filter_by(
                muscle_group_id=form.muscle_group.data
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

    except Exception as e:
        flash(
            "An error has occurred. Please try again.",
            "error"
        )

    return render_template(
        "exercise/exercises.html", form=form, isNew=True, progress_id=0
    )


@app.route("/get_exercises", methods=["GET"])
@login_required
def get_exercises():
    """
    Provide a list of exercises based on the selected muscle group.

    This route is called via AJAX to dynamically populate the exercise
    options in the exercise log form based on the selected muscle group.

    Returns:
    JSON: A list of exercises corresponding to the selected muscle group.
    """
    try:
        muscle_group_id = request.args.get("muscle_group_id")
        muscle_group = MuscleGroups.query.get(muscle_group_id)
        return jsonify(muscle_group.exercises)
    except Exception as e:
        flash(
            "An error has occurred. Please try again.",
            "error",
        )


@app.route("/log/<int:progress_id>", methods=["GET", "POST"])
@login_required
def log_edit(progress_id):
    """
    Handle the editing of an existing exercise log.

    This route allows users to edit their previously logged exercises.
    It fetches an existing exercise log by its ID and allows the user
    to modify and update it.

    Returns:
    Template or Redirection: Renders the exercise log form for editing
    or redirects to the log page after successful update.
    """
    try:
        progress = Progress.query.filter_by(
            id=progress_id, user_id=current_user.id
        ).first()

        if not progress:
            flash(
                "Exercise not found or you do not have permission to edit it.",
                "error",
            )
            return redirect(url_for("log"))

        form = ExerciseLogForm(
            obj=progress if flask.request.method == "GET" else None
        )

        # Create the muscle group options
        muscle_groups = MuscleGroups.query.all()
        form.muscle_group.choices = [(0, "Select a muscle group")] + [
            (mg.id, mg.name) for mg in muscle_groups
        ]

        # Create the exercise options
        exercises = Exercises.query.filter_by(
            muscle_group_id=progress.muscle_group_id
        ).all()
        form.exercises.choices = [(0, "Select an exercise")] + [
            (ex.id, ex.name) for ex in exercises
        ]

        if flask.request.method == "POST":
            if form.validate_on_submit():
                progress.muscle_group_id = form.muscle_group.data
                progress.exercise_id = form.exercises.data
                progress.weight = form.weight.data
                progress.sets = form.sets.data
                progress.reps = form.reps.data
                progress.notes = form.notes.data
                db.session.commit()
                flash("Exercise log updated successfully!", "success")
        else:
            form.muscle_group.data = progress.muscle_group_id
            form.exercises.data = progress.exercise_id

    except Exception as e:
        flash(
            "An error has occurred. Please try again.",
            "error",
        )

    return render_template(
        "exercise/exercises.html", form=form, isNew=False,
        progress_id=progress_id
    )


@app.route("/log/<int:progress_id>/delete", methods=["GET", "POST"])
@login_required
def log_delete(progress_id):
    """
    Handle the deletion of an exercise log.

    This route allows users to delete their exercise logs. It deletes
    the log identified by its ID and provides feedback to the user
    upon successful deletion.

    Returns:
    Redirection: Redirects to the dashboard page after the exercise
    log is deleted.
    """
    try:
        progress = Progress.query.filter_by(
            id=progress_id, user_id=current_user.id
        ).first()

        if not progress:
            flash(
                "Exercise not found or deletion permission denied.",
                "error",
            )
            return redirect(url_for("dashboard"))

        db.session.delete(progress)
        db.session.commit()
        flash("Exercise Deleted Successfully!", "success")

    except Exception as e:
        flash(
            "An error has occurred. Please try again.",
            "error",
        )

    return redirect(url_for("dashboard"))
