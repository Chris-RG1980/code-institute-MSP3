import json

from muscle_metrics.models.exercises import Exercises
from muscle_metrics.models.muscle_groups import MuscleGroups

from . import db


def add_muscle_group(name):
    existing_group = MuscleGroups.query.filter_by(name=name).first()
    if existing_group:
        return existing_group

    new_group = MuscleGroups(name=name)
    db.session.add(new_group)
    return new_group


def populate_muscle_groups_from_json(file_path):
    with open(file_path, "r") as file:
        muscle_groups_data = json.load(file)

        for group_data in muscle_groups_data:
            name = group_data.get("name")
            if name:
                add_muscle_group(name)

        db.session.commit()


def add_exercises(name, muscle_group_id):
    existing_exercise = Exercises.query.filter_by(name=name).first()
    if existing_exercise:
        return existing_exercise

    new_exercise = Exercises(name=name, muscle_group_id=muscle_group_id)
    db.session.add(new_exercise)
    return new_exercise


def populate_exercises_from_json(file_path):
    with open(file_path, "r") as file:
        exercises_data = json.load(file)

        for exercise_data in exercises_data:
            name = exercise_data.get("name")
            muscle_group_id = exercise_data.get("muscle_group_id")
            if name and muscle_group_id:
                add_exercises(name, muscle_group_id)

        db.session.commit()


populate_muscle_groups_from_json("muscle_metrics/static/json/muscle_groups.json")
populate_exercises_from_json("muscle_metrics/static/json/exercises.json")
