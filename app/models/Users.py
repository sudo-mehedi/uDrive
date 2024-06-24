from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin
from app.models import db


class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str]
    password: Mapped[str]

