from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, logout_user
from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SelectField, SubmitField, TextAreaField
from wtforms.validators import InputRequired

from muscle_metrics import app, db, login_manager
from muscle_metrics.models import Progress, User

from .dashboard import routes
from .exercise_log import routes
from .home import routes
from .login import routes
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
