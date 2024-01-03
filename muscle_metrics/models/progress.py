import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from muscle_metrics import db


class Progress(db.Model):
    __tablename__ = "progress"
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    # user_id = db.Column(
    #     UUID(as_uuid=True),
    #     db.ForeignKey("users.id", ondelete="CASCADE"),
    #     default=uuid.uuid4,
    #     nullable=False,
    # )
    exercise_id = db.Column(
        db.Integer(), db.ForeignKey("exercises.id", ondelete="CASCADE"), nullable=False
    )
    weight = db.Column(db.Integer(), nullable=False)
    reps = db.Column(db.Integer(), nullable=False)
    sets = db.Column(db.Integer(), nullable=False)
    date_added = db.Column(
        db.DateTime(timezone=True), onupdate=func.now(), nullable=False
    )

    def __repr__(self):
        return (
            self.id,
            # self.user_id,
            self.exercise_id,
            self.weight,
            self.reps,
            self.sets,
            self.date_added,
        )
