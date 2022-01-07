from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from dataclasses import dataclass


@dataclass
class StudentSubjectModel(db.Model):
    
    id: int
    subject_id: int
    student_id: int
    
    __tablename__ = 'student_subject'
    
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subjects.id', ondelete='cascade'), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='cascade'), nullable=False)
    time_course = Column(String(20), nullable=False)