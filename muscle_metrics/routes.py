from flask import flash, redirect, render_template, url_for
from flask_login import login_required, logout_user

from muscle_metrics import app, db, login_manager, mongo
from muscle_metrics.models.users import User

from .home import routes
from .login import routes
from .models import users
from .profile import routes
from .register import routes


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


@app.route("/get_muscle_groups")
@login_required
def get_muscle_groups():
    muscles = mongo.db.muscle_groups.find()
    return render_template("exercise/exercises.html", muscles=muscles)


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
