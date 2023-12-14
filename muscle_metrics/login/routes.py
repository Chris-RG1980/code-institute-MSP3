from flask import flash, redirect, render_template, url_for
from flask_login import login_user

from muscle_metrics import app, bcrypt, db
from muscle_metrics.models import User

from .forms import LoginForm


# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # Form Validation
    if form.validate_on_submit():
        user: User = db.session.query(User).filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("Login successful", "success")
                return redirect(url_for("get_muscle_groups"))
            else:
                flash("Incorrect email or password. Please try again!", "error")
        else:
            flash("Incorrect email or password. Please try again!", "error")

    return render_template("login/login.html", form=form)
