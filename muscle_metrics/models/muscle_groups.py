import json

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


def add_muscle_group(name):
    existing_group = MuscleGroups.query.filter_by(name=name).first()
    if existing_group:
        return existing_group

    new_group = MuscleGroups(name=name)
    db.session.add(new_group)
    return new_group


def populate_from_json(file_path):
    with open(file_path, "r") as file:
        muscle_groups_data = json.load(file)

        for group_data in muscle_groups_data:
            name = group_data.get("name")
            if name:
                add_muscle_group(name)

        db.session.commit()


json_file_path = "muscle_metrics/static/json/muscle_groups.json"
populate_from_json(json_file_path)
