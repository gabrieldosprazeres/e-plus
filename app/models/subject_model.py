from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass


@dataclass
class SubjectModel(db.Model):
    
    id: int
    subject: str
    
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    subject = Column(String(50), nullable=False, unique=True)