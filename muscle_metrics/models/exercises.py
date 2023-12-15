from muscle_metrics import db


class Exercises(db.Model):
    __tablename__ = "exercises"
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    muscle_groups_id = db.Column(
        db.Integer(),
        db.ForeignKey("muscle_groups.id", ondelete="CASCADE"),
        nullable=False,
    )

    def __repr__(self):
        return (self.id, self.name, self.muscle_groups_id)
