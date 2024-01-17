import uuid

from flask_login import current_user
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from muscle_metrics import db
from muscle_metrics.models import exercises


class Progress(db.Model):
    __tablename__ = "progress"
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    user_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    exercise_id = db.Column(db.Integer(), db.ForeignKey("exercises.id"), nullable=False)
    weight = db.Column(db.Float(), nullable=False)
    reps = db.Column(db.Integer(), nullable=False)
    sets = db.Column(db.Integer(), nullable=False)
    notes = db.Column(db.String(), nullable=True)
    date_added = db.Column(
        db.DateTime(timezone=True), onupdate=func.now(), nullable=False
    )

    exercise = relationship("Exercises", back_populates="progress")

    def __repr__(self):
        return (
            self.id,
            self.user_id,
            self.exercise_id,
            self.weight,
            self.reps,
            self.sets,
            self.notes,
            self.date_added,
        )
