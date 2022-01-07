from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
    
    from app.models.student_model import StudentModel
    from app.models.address_model import AddressModel
    from app.models.phone_model import PhoneModel
    from app.models.subject_model import SubjectModel
    from app.models.student_subject_model import StudentSubjectModel
    
    Migrate(app, app.db)