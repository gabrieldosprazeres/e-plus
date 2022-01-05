from app.configs.database import db
from sqlalchemy import Column, Integer, String, DateTime
from dataclasses import dataclass
from datetime import datetime


@dataclass
class StudentModel(db.Model):

    id: int
    full_name: str
    age: int
    phone: str
    created_at: str

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    phone = Column(String(14), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow())