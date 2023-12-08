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
            Length(
                min=2,
                max=50,
            ),
        ],
        description="Maximum 50 characters",
    )

    last_name = StringField(
        "Last Name",
        [
            InputRequired(),
            Length(
                min=2,
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


@app.route("/")
def home():
    return render_template("index.html")


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
        )
        db.session.add(user)
        db.session.commit()
        flash("Successfully registered, please login", "success")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


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
