import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_bcrypt import Bcrypt
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo, ValidationError
from datetime import datetime
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from muscle_metrics import app, db, mongo, bcrypt, login_manager
from muscle_metrics.models.users import User
from flask_login import (
    login_user,
    login_required,
    logout_user,
    current_user,
)
import sys


# Create login form
class LoginForm(FlaskForm):
    email = EmailField(
        "Email Address",
        [
            Email(),
            InputRequired(),
        ],
        render_kw={"placeholder": "email@address.com"},
    )
    password = PasswordField(
        "Password",
        [
            InputRequired(),
        ],
    )
    submit = SubmitField("")


# Create registration form
class RegistrationForm(FlaskForm):
    first_name = StringField(
        "First Name",
        [
            InputRequired(),
            Length(max=50),
        ],
        description="Maximum 50 characters",
    )

    last_name = StringField(
        "Last Name",
        [
            InputRequired(),
            Length(
                max=50,
            ),
        ],
        description="Maximum 50 characters",
    )
    email = EmailField(
        "Email Address",
        [
            Email(),
            InputRequired(),
        ],
        render_kw={"placeholder": "email@address.com"},
    )
    password = PasswordField(
        "Password",
        [
            InputRequired(),
            EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Confirm Password", [InputRequired()])
    submit = SubmitField("Register")


class FirstNameForm(FlaskForm):
    first_name = RegistrationForm.first_name


class LastNameForm(FlaskForm):
    last_name = RegistrationForm.last_name


class EmailForm(FlaskForm):
    email = RegistrationForm.email


class PasswordForm(FlaskForm):
    currentPassword = PasswordField("Current Password", [InputRequired()])
    password = PasswordField(
        "Password",
        [
            InputRequired(),
            EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Confirm Password", [InputRequired()])


@app.route("/")
def home():
    return render_template("index.html")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():
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

    return render_template("register.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@app.route("/profile/<id>", methods=["GET"])
def edit_profile(id):
    form = RegistrationForm()
    passwordForm = PasswordForm()
    user = User.query.get_or_404(id)

    return render_template(
        "edit_profile.html",
        form=form,
        passwordForm=passwordForm,
        user=user,
    )


@app.route("/profile/<id>/fname", methods=["POST"])
def edit_profile_fname(id):
    form = FirstNameForm()
    user = User.query.get_or_404(id)

    if form.validate_on_submit():
        user.first_name = request.form["first_name"]
        updateUser()

    return redirect(url_for("edit_profile", id=user.id))


@app.route("/profile/<id>/lname", methods=["POST"])
def edit_profile_lname(id):
    form = LastNameForm()
    user = User.query.get_or_404(id)

    if form.validate_on_submit():
        user.last_name = request.form["last_name"]
        updateUser()

    return redirect(url_for("edit_profile", id=user.id))


@app.route("/profile/<id>/email", methods=["POST"])
def edit_profile_email(id):
    form = EmailForm()
    user = User.query.get_or_404(id)

    if form.validate_on_submit():
        user.email = request.form["email"]
        updateUser()

    return redirect(url_for("edit_profile", id=user.id))


@app.route("/profile/<id>/password", methods=["POST"])
def edit_profile_password(id):
    form = PasswordForm()
    user = User.query.get_or_404(id)

    # Form Validation
    if form.validate_on_submit():
        if user:
            if bcrypt.check_password_hash(user.password, form.currentPassword.data):
                hashed_password = bcrypt.generate_password_hash(
                    form.password.data.encode("utf8")
                ).decode("utf8")
                user.password = hashed_password
                try:
                    db.session.commit()
                    flash("Password updated successfully", "success")
                except:
                    flash("Error! Looks like there was a problem...Try again", "error")
            else:
                flash("Incorrect current password. Please try again.", "error")
                return redirect(url_for("edit_profile", id=user.id))
        else:
            flash("User not found.", "error")
            return redirect(url_for("home"))
    else:
        message = ""
        for error in form.password.errors:
            message += error + "\n"

        flash(message, "error")

    return redirect(url_for("edit_profile", id=user.id))


def updateUser():
    try:
        db.session.commit()
        flash("Updated successfully", "success")
    except:
        flash("Error! Looks like there was a problem...Try again", "error")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # Form Validation
    if form.validate_on_submit():
        user = db.session.query(User).filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("Login successful", "success")
                return redirect(url_for("get_muscle_groups"))
            else:
                flash("Incorrect email or password. Please try again!", "error")
        else:
            flash("Incorrect email or password. Please try again!", "error")

    return render_template("login.html", form=form)


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
    return render_template("exercises.html", muscles=muscles)


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
