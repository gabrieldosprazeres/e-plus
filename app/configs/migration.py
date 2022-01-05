from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
    
    from app.models.student_model import StudentModel
    
    Migrate(app, app.db)