from app.configs.database import db
from sqlalchemy import Column, Integer, String
from dataclasses import dataclass
from sqlalchemy.orm import relationship


@dataclass
class SubjectModel(db.Model):
    
    subject: str
    
    __tablename__ = 'subjects'
    
    id = Column(Integer, primary_key=True)
    subject = Column(String(50), nullable=False, unique=True)
    
    student = relationship('StudentModel', secondary='student_subject', backref='subjects')