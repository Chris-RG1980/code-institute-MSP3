from flask import render_template
from flask_login import current_user, login_required

from muscle_metrics import app
from muscle_metrics.models import Progress


@app.route("/dashboard", methods=["GET"])
@login_required
def dashboard():
    user_id = current_user.id
    user_progress = (
        Progress.query.filter_by(user_id=user_id)
        .order_by(Progress.date_added.desc())
        .all()
    )

    return render_template("dashboard/dashboard.html", user_progress=user_progress)
