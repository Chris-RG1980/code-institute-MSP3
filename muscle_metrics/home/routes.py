from flask import render_template

from muscle_metrics import app


@app.route("/")
def home():
    return render_template("home/index.html")
