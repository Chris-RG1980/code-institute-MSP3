import uuid

from flask_login import UserMixin
from sqlalchemy import Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from muscle_metrics import db


class User(db.Model, UserMixin):
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
    is_deleted = db.Column(Boolean, default=False, nullable=False)

    def __repr__(self):
        return (
            self.id,
            self.first_name,
            self.last_name,
            self.email,
            self.password,
            self.created_date_time,
            self.is_deleted,
            self.last_modified_date_time,
        )
