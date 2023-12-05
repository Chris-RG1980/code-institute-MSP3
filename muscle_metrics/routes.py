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
    first_name = StringField("First Name", [InputRequired(), Length(min=1, max=50)])
    last_name = StringField("Last Name", [InputRequired(), Length(min=1, max=50)])
    email = EmailField("Email Address", [Email(), InputRequired()])
    password = PasswordField(
        "New Password",
        [InputRequired(), EqualTo("confirm", message="Passwords must match")],
    )
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("Register")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    # Form validation
    if request.method == "POST" and form.validate():
        hashed_password = bcrypt.hashpw(
            request.form["password"].encode("utf-8"), bcrypt.gensalt()
        )

        user = User(
            first_name=request.form["first_name"],
            last_name=request.form["last_name"],
            email=request.form["email"],
            password=hashed_password.decode("utf-8"),
            created_date_time=datetime.now(),
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/get_muscle_groups")
def get_muscle_groups():
    muscles = mongo.db.muscle_groups.find()
    return render_template("exercises.html", muscles=muscles)
