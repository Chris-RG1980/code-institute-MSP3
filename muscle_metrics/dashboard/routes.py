from datetime import datetime, timedelta

from flask import render_template
from flask_login import current_user, login_required
from sqlalchemy import func

from muscle_metrics import app, db
from muscle_metrics.models import Progress
from muscle_metrics.models.muscle_groups import MuscleGroups


@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    user_id = current_user.id
    user_progress = (
        Progress.query.filter_by(user_id=user_id)
        .order_by(Progress.date_added.desc())
        .all()
    )

    muscleGroupChartData = (
        db.session.query(MuscleGroups.name, func.count(Progress.id))
        .join(MuscleGroups, Progress.muscle_group_id == MuscleGroups.id)
        .filter(Progress.user_id == user_id)
        .group_by(MuscleGroups.name)
        .all()
    )

    muscleGroupChartLabels = [item[0] for item in muscleGroupChartData]
    muscleGroupChartValues = [item[1] for item in muscleGroupChartData]

    last_week = datetime.utcnow() - timedelta(weeks=1)
    exerciseNumberChartData = (
        db.session.query(
            func.extract("DAY", Progress.date_added), func.count(Progress.id)
        )
        .filter(Progress.date_added >= last_week)
        .filter(Progress.user_id == user_id)
        .group_by(func.extract("DAY", Progress.date_added))
        .all()
    )

    # Get today's date
    end_date = datetime.now().date()

    # Calculate the start date as 6 days ago from today
    start_date = end_date - timedelta(days=6)

    # Create an array of dates for the last 7 days including today
    date_range = [start_date + timedelta(days=i) for i in range(7)]
    day_numbers = [date.day for date in date_range]
    data_dict = dict(exerciseNumberChartData)

    # Initialize a new array with default value 0
    exerciseNumberChartValues = [0] * len(day_numbers)

    # Loop through the last 7 days and populate the new array
    for i, day in enumerate(day_numbers):
        if day in data_dict:
            exerciseNumberChartValues[i] = data_dict[day]

    exerciseNumberChartLabels = [date.strftime("%A") for date in date_range]

    return render_template(
        "dashboard/dashboard.html",
        user_progress=user_progress,
        muscleGroupChartLabels=muscleGroupChartLabels,
        muscleGroupChartValues=muscleGroupChartValues,
        exerciseNumberChartLabels=exerciseNumberChartLabels,
        exerciseNumberChartValues=exerciseNumberChartValues,
        exerciseNumberChartData=exerciseNumberChartData,
    )
