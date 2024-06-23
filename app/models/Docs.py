from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models import db

class Folders(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    parent_id: Mapped[int] = mapped_column(Integer, ForeignKey('folders.id'))
    children = relationship("Folders")
    user_root:Mapped[str] = mapped_column(nullable=True)



# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(unique=True)
#     email: Mapped[str]
#     password: Mapped[str]








