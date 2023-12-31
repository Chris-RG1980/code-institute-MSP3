import json

from muscle_metrics import db


class MuscleGroups(db.Model):
    __tablename__ = "muscle_groups"
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    exercises = db.relationship("Exercises")

    def __repr__(self):
        return (self.id, self.name, self.exercises)
