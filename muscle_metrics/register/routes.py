from datetime import datetime

from flask import flash, redirect, render_template, request, url_for

from muscle_metrics import app, bcrypt, db
from muscle_metrics.models import User

from .forms import RegistrationForm


@app.route("/register", methods=["GET", "POST"])
def register():
    """
    Handle the user registration process.

    This route displays a registration form and processes its submission. It includes
    validation to check if the email already exists in the database. If validation passes,
    it creates a new User object, hashes the password for security, and saves the user to
    the database. After successful registration, it redirects the user to the login page.

    Returns:
    Template or Redirection: Renders the registration form template or redirects to the login page after successful registration.
    """
    form = RegistrationForm()

    # Form validation
    if form.validate_on_submit():
        email = request.form["email"].lower()
        existing_user = db.session.query(User).filter_by(email=email).first()

        if existing_user:
            flash("Email Already Exists", "email_error")
            return redirect(url_for("register"))

        hashed_password = bcrypt.generate_password_hash(
            request.form["password"].encode("utf8")
        ).decode("utf8")

        user = User(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=email,
            password=hashed_password,
            created_date_time=datetime.now(),
            last_modified_date_time=datetime.now(),
        )
        db.session.add(user)
        db.session.commit()
        flash("Successfully registered, please login", "success")
        return redirect(url_for("login"))

    return render_template("register/register.html", form=form)
