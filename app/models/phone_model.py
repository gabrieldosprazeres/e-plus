from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from dataclasses import dataclass


@dataclass
class PhoneModel(db.Model):
    
    id: int
    name: str
    phone_number: str
    
    __tablename__ = 'phones'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone_number = Column(String(14), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='cascade'), nullable=False)
    
    student = relationship('StudentModel', backref='phones')