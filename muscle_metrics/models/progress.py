import uuid

from flask_login import current_user
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from muscle_metrics import db
from muscle_metrics.models import exercises


class Progress(db.Model):
    """
    Data model for the user to track their progress.

    This model stores details about the exercises performed by users, including
    the weight used, repetitions, and sets, along with any notes and timestamps.

    """

    __tablename__ = "progress"

    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    user_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    muscle_group_id = db.Column(
        db.Integer(), db.ForeignKey("muscle_groups.id"), nullable=False
    )
    exercise_id = db.Column(db.Integer(), db.ForeignKey("exercises.id"), nullable=False)
    weight = db.Column(db.Float(), nullable=False)
    reps = db.Column(db.Integer(), nullable=False)
    sets = db.Column(db.Integer(), nullable=False)
    notes = db.Column(db.String(), nullable=True)
    date_added = db.Column(
        db.DateTime(timezone=True), default=func.now(), nullable=False
    )
    date_modified = db.Column(
        db.DateTime(timezone=True), onupdate=func.now(), nullable=True
    )

    exercise = relationship("Exercises", back_populates="progress")
    muscle_group = relationship("MuscleGroups", backref="progress")

    def __repr__(self):
        """Represent the progress instance as a string."""
        return (
            self.id,
            self.user_id,
            self.muscle_group_id,
            self.exercise_id,
            self.weight,
            self.reps,
            self.sets,
            self.notes,
            self.date_added,
            self.date_modified,
        )
