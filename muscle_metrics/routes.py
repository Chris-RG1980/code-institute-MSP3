import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo
from datetime import datetime
from muscle_metrics import app, db, mongo
from muscle_metrics.models.users import User
import bcrypt


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

        hashed_password = bcrypt.hashpw(
            request.form["password"].encode("utf-8"), bcrypt.gensalt()
        )

        user = User(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=email,
            password=hashed_password.decode("utf-8"),
            created_date_time=datetime.now(),
        )
        db.session.add(user)
        db.session.commit()
        flash("Successfully registered, please login", "success")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/get_muscle_groups")
def get_muscle_groups():
    muscles = mongo.db.muscle_groups.find()
    return render_template("exercises.html", muscles=muscles)
