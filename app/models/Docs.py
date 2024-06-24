from sqlalchemy import Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models import db
from typing import List, Dict, Optional

class Folders(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    parent_id: Mapped[int] = mapped_column(Integer, ForeignKey('folders.id'))
    children = relationship("Folders", back_populates="parent")
    parent = relationship("Folders", back_populates="children", remote_side=[id])
    user_root:Mapped[str] = mapped_column(nullable=True)

    created_by:Mapped[int]


    @classmethod
    def get_path_with_ids(cls, folder_id: int) -> Optional[List[Dict[str, str]]]:
        folder = cls.query.get(folder_id)
        if folder is None:
            return None
        
        path_parts = []
        current = folder
        while current:
            path_parts.append({"id": str(current.id), "name": current.name})
            current = current.parent
        
        return list(reversed(path_parts)) 
# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(unique=True)
#     email: Mapped[str]
#     password: Mapped[str]


import datetime
from sqlalchemy.sql import func
class Files(db.Model):
    id:Mapped[int]  = mapped_column(primary_key=True)
    name:Mapped[str]
    size: Mapped[int] = mapped_column(nullable=True)
    file_type: Mapped[int] = mapped_column(nullable=True)
    parent_id:Mapped[int]
    path: Mapped[str]

    created_by:Mapped[int] = mapped_column(nullable=True)
    
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )