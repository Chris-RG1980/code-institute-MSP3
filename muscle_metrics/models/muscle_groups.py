import json

from muscle_metrics import db


class MuscleGroups(db.Model):
    """
    Data model for muscle groups.

    Each muscle group is associated with multiple exercises.

    """

    __tablename__ = "muscle_groups"

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    exercises = db.relationship("Exercises")

    def __repr__(self):
        """Represent the muscle group instance as a string."""
        return (self.id, self.name, self.exercises)
