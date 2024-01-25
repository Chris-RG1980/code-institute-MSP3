import json
from dataclasses import dataclass

from flask import flash
from sqlalchemy.orm import relationship

from muscle_metrics import db


@dataclass
class Exercises(db.Model):
    """
    Data model for exercises.
    """

    id: int
    name: str

    __tablename__ = "exercises"

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    muscle_group_id = db.Column(db.Integer(), db.ForeignKey("muscle_groups.id"))

    progress = relationship("Progress", back_populates="exercise")

    def __repr__(self):
        """Represent the exercise instance as a string."""
        return (self.id, self.name, self.muscle_group_id)


def add_exercises(name, muscle_group_id):
    """
    Adds a new exercise to the database or retrieves it if already exists.

    Returns:
        An instance of the exercise.
    """
    try:
        existing_exercise = Exercises.query.filter_by(name=name).first()

        if existing_exercise:
            return existing_exercise

        new_exercise = Exercises(name=name, muscle_group_id=muscle_group_id)
        db.session.add(new_exercise)
        return new_exercise
    except:
        return "Error occurred while adding the exercise."


def populate_from_json(file_path):
    """
    Populates the database with exercises data from a JSON file.
    """
    try:
        with open(file_path, "r") as file:
            exercises_data = json.load(file)

            for exercise_data in exercises_data:
                name = exercise_data.get("name")
                muscle_group_id = exercise_data.get("muscle_group_id")

                if name and muscle_group_id:
                    add_exercises(name, muscle_group_id)

            db.session.commit()
    except:
        return "An unexpected error occurred."
