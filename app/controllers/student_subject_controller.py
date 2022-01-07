from flask import request, jsonify, current_app
from app.models.student_subject_model import StudentSubjectModel
from app.models.subject_model import SubjectModel


def student_registration_subject(student_id: int):
    data: dict = request.get_json()
    
    subject = data.pop('subject')
    
    subject = SubjectModel.query.filter_by(subject=subject).first()
    
    data['subject_id'] = subject.id
    data['student_id'] = student_id
    
    registration = StudentSubjectModel(**data)
    
    current_app.db.session.add(registration)
    current_app.db.session.commit()
    
    return jsonify(
        {
			'message': 'Subject successfully registered!'
		}
        ), 201