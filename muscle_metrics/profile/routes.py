from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from muscle_metrics import app, bcrypt, db
from muscle_metrics.models import User
from muscle_metrics.register.forms import RegistrationForm

from .forms import ChangePasswordForm, EmailForm, FirstNameForm, LastNameForm


# User Profile Page
@app.route("/profile/<id>", methods=["GET"])
def edit_profile(id):
    form = RegistrationForm()
    passwordForm = ChangePasswordForm()
    user = User.query.get_or_404(id)

    return render_template(
        "profile/edit_profile.html",
        form=form,
        passwordForm=passwordForm,
        user=user,
    )


# Edit User First Name
@app.route("/profile/<id>/fname", methods=["POST"])
def edit_profile_fname(id):
    form = FirstNameForm()
    user: User = User.query.get_or_404(id)

    if form.validate_on_submit():
        user.first_name = request.form["first_name"]
        updateUser()

    return redirect(url_for("edit_profile", id=user.id))


# Edit User Last Name
@app.route("/profile/<id>/lname", methods=["POST"])
def edit_profile_lname(id):
    form = LastNameForm()
    user: User = User.query.get_or_404(id)

    if form.validate_on_submit():
        user.last_name = request.form["last_name"]
        updateUser()

    return redirect(url_for("edit_profile", id=user.id))


# Edit User Email
@app.route("/profile/<id>/email", methods=["POST"])
def edit_profile_email(id):
    form = EmailForm()
    user: User = User.query.get_or_404(id)

    if form.validate_on_submit():
        user.email = request.form["email"]
        updateUser()

    return redirect(url_for("edit_profile", id=user.id))


# Update User function used in Edit first name, edit last name & edit email
def updateUser():
    try:
        db.session.commit()
        flash("Updated successfully", "success")
    except:
        flash("Error! Looks like there was a problem...Try again", "error")


# Change User Password
@app.route("/profile/<id>/password", methods=["POST"])
def edit_profile_password(id):
    form = ChangePasswordForm()
    user: User = User.query.get_or_404(id)

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


# Delete User Account
@app.route("/profile/<id>/delete", methods=["GET"])
@login_required
def delete_user(id):
    if id == str(current_user.id):
        user = User.query.get_or_404(id)

        try:
            db.session.delete(user)
            db.session.commit()
            flash("User Deleted Successfully!", "success")
            return redirect(url_for("home"))
        except:
            flash("There was a problem deleting user, try again..", "error")
    else:
        flash("Sorry, you can't delete that user!", "error")

    return redirect(url_for("edit_profile", id=current_user.id))
