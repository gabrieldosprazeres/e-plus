from app.configs.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from dataclasses import dataclass
from sqlalchemy.orm import relationship


@dataclass
class AddressModel(db.Model):
    
    state: str
    city: str
    district: str
    street: str
    house_number: str
    complement: str

    __tablename__ = 'address'
    
    id = Column(Integer, primary_key=True)
    state = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    district = Column(String(50), nullable=False)
    street = Column(String(50), nullable=False)
    house_number = Column(String(5), nullable=False)
    complement = Column(String(100), nullable=False)
    student_id = Column(Integer, ForeignKey('students.id', ondelete='cascade'), nullable=False, unique=True)
    
    student = relationship('StudentModel', backref='address', uselist=False)