from muscle_metrics import db


class MuscleGroups(db.Model):
    __tablename__ = "muscle_groups"
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    exercises = db.relationship(
        "Exercises", backref="muscle_groups", cascade="all, delete", lazy=True
    )

    def __repr__(self):
        return (self.id, self.name, self.exercises)


muscle_group_1 = MuscleGroups(name="Arms")
muscle_group_2 = MuscleGroups(name="Back")
muscle_group_3 = MuscleGroups(name="Chest")
muscle_group_4 = MuscleGroups(name="Core")
muscle_group_5 = MuscleGroups(name="Legs")
muscle_group_6 = MuscleGroups(name="Shoulders")

db.session.add(muscle_group_1)
db.session.add(muscle_group_2)
db.session.add(muscle_group_3)
db.session.add(muscle_group_4)
db.session.add(muscle_group_5)
db.session.add(muscle_group_6)
db.session.commit()
