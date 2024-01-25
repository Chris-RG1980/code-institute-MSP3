from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from muscle_metrics import app, bcrypt, db
from muscle_metrics.models import User
from muscle_metrics.register.forms import RegistrationForm

from .forms import ChangePasswordForm, EmailForm, FirstNameForm, LastNameForm


# User Profile Page
@app.route("/profile/<id>", methods=["GET"])
def edit_profile(id):
    """
    Render the user profile edit page.

    This route displays a form allowing the user to edit their profile information,
    including changing their first name, last name, email, and password.

    Returns:
    Template: Renders the user profile edit page template.
    """
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
    """
    Handle the editing of the user's first name.

    This route processes the form submission for changing the user's first name.

    Returns:
    Redirection: Redirects to the profile edit page after updating the first name.
    """
    form = FirstNameForm()
    user: User = User.query.get_or_404(id)

    if form.validate_on_submit():
        user.first_name = request.form["first_name"]
        updateUser()

    return redirect(url_for("edit_profile", id=user.id))


# Edit User Last Name
@app.route("/profile/<id>/lname", methods=["POST"])
def edit_profile_lname(id):
    """
    Handle the editing of the user's last name.

    This route processes the form submission for changing the user's last name.

    Returns:
    Redirection: Redirects to the profile edit page after updating the last name.
    """
    form = LastNameForm()

    user: User = User.query.get_or_404(id)

    if form.validate_on_submit():
        user.last_name = request.form["last_name"]
        updateUser()

    return redirect(url_for("edit_profile", id=user.id))


# Edit User Email
@app.route("/profile/<id>/email", methods=["POST"])
def edit_profile_email(id):
    """
    Handle the editing of the user's email address.

    This route processes the form submission for changing the user's email address.

    Returns:
    Redirection: Redirects to the profile edit page after updating the email.
    """
    form = EmailForm()
    user: User = User.query.get_or_404(id)

    if form.validate_on_submit():
        new_email = request.form["email"].lower()

        if user.email != new_email:
            try:
                existing_user = (
                    db.session.query(User).filter_by(email=new_email).first()
                )
            except:
                flash("Error! Looks like there was a problem...Try again", "error")

            if existing_user:
                flash("Email already exists", "error")
            else:
                user.email = new_email
                updateUser()
        else:
            flash("Email must be different from your current email", "error")

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
    """
    Handle the changing of the user's password.

    This route processes the form submission for changing the user's password. It validates
    the current password and updates it with the new password if validation is successful.

    Returns:
    Redirection: Redirects to the profile edit page after attempting to update the password.
    """
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
    """
    Handle the deletion of a user account.

    This route allows a user to delete their own account. It verifies the user's identity
    and then proceeds to delete the account if the user is authenticated to do so.

    Returns:
    Redirection: Redirects to the home page after deleting the user account.
    """
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
