from flask import render_template

from muscle_metrics import app


@app.route("/")
def home():
    """
    Render the home page of the application.

    This route handles the main landing page of the application.
    It serves the home page when a user visits the root URL ('/').

    Returns:
    Template: Renders the home page template.
    """
    return render_template("home/index.html")
