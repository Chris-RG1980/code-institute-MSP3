from muscle_metrics import db


class Exercises(db.Model):
    __tablename__ = "exercises"
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    muscle_groups = db.relationship(
        "MuscleGroups", backref="exercises", cascade="all, delete", lazy=True
    )

    def __repr__(self):
        return (self.id, self.name, self.muscle_groups)
