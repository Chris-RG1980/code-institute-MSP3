from flask import flash, redirect, render_template, url_for
from flask_login import login_user

from muscle_metrics import app, bcrypt, db
from muscle_metrics.models import User

from .forms import LoginForm


@app.route("/login", methods=["GET", "POST"])
def login():
    """
    Handle the login process for a user.

    This route allows users to log in to the application using their email and password.
    It validates the user's credentials, logs them in upon success, and redirects to the dashboard.
    If the login is unsuccessful, it flashes an error message and reloads the login page.

    Returns:
    Template or Redirection: Renders the login page template on GET request or invalid form submission.
    Redirects to the dashboard upon successful login.
    """
    form = LoginForm()

    # Form Validation
    if form.validate_on_submit():
        user: User = db.session.query(User).filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for("dashboard"))
        else:
            flash("Incorrect email or password. Please try again!", "error")

    return render_template("login/login.html", form=form)
