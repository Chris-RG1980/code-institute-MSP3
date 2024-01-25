# Import necessary modules from Flask and its extensions
from flask import abort, flash, redirect, render_template, url_for
from flask_login import login_required, logout_user

# Import application, database, and login manager from muscle_metrics package
from muscle_metrics import app, db, login_manager

# Import the User models from the models module
from muscle_metrics.models import User

# Import routes from different modules within the application
from .dashboard import routes
from .exercise_log import routes
from .home import routes
from .login import routes
from .profile import routes
from .register import routes


@login_manager.user_loader
def load_user(user_id):
    """
    Load a user from the database given their user_id.

    This function is used by Flask-Login to manage user sessions.
    """
    try:
        user = db.session.query(User).get(user_id)
    except:
        abort(401)

    return user


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    """
    Log out the current user and redirect to the home page.

    This route handles the logout functionality and provides feedback to the user upon successful logout.
    """
    logout_user()
    flash("You have been logged out!", "success")
    return redirect(url_for("home"))


@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error handler for 404 Not Found errors.

    This function renders a custom 404 error page when a user tries to access a non-existent page.
    """
    return render_template("404.html"), 404


@app.errorhandler(401)
def unauthorised_access(e):
    """
    Custom error handler for 401 Unauthorized Access errors.

    This function renders a custom 401 error page when a user tries to access a resource they are not authorized to.
    """
    return render_template("401.html"), 401


@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom error handler for 500 Internal Server Error.

    This function renders a custom 500 error page in the event of an internal server error.
    """
    return render_template("500.html"), 500
