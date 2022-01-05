from flask import request, jsonify, current_app

from app.models.student_model import StudentModel


def registering_student():
    data = request.get_json()
    
    student = StudentModel(**data)
    
    current_app.db.session.add(student)
    current_app.db.session.commit()
    
    return jsonify(student), 201