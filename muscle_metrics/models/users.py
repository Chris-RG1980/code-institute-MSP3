import uuid

from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from muscle_metrics import db


class User(db.Model, UserMixin):
    """
    Data model for user accounts.

    This model includes personal information of the user, such as their
    name and email, along with password. It also tracks the creation
    and last modification times of the user's account.
    """

    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(72), nullable=False)
    created_date_time = db.Column(db.DateTime(timezone=True), nullable=False)
    last_modified_date_time = db.Column(
        db.DateTime(timezone=True), onupdate=func.now(), nullable=False
    )

    progress = db.relationship(
        "Progress", backref="user", cascade="all, delete", lazy=True
    )

    def __repr__(self):
        """Represent the user instance as a string."""
        return (
            self.id,
            self.first_name,
            self.last_name,
            self.email,
            self.password,
            self.created_date_time,
            self.progress,
            self.last_modified_date_time,
        )
