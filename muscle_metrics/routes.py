import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from muscle_metrics import app, db, mongo


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/get_muscle_groups")
def get_muscle_groups():
    muscles = mongo.db.muscle_groups.find()
    return render_template("exercises.html", muscles=muscles)
