from flask import request, jsonify, current_app
from flask_jwt_extended import get_jwt_identity
from app.controllers import check_key_for_subject_register, check_subject_existing, check_type_for_subject_register
from app.excepetions.student_subject_exception import InvalidKeySubjectRegisterError, InvalidTypeSubjectRegisterError
from app.excepetions.subject_exception import SubjectNotFoundError
from app.models.subject_model import SubjectModel
from app.models.student_subject_model import StudentSubjectModel


def student_registration_subject():
    data: dict = request.get_json()
    student: dict = get_jwt_identity()
    
    try:
        check_key_for_subject_register(data)
        check_type_for_subject_register(data)

        subject_name = data.pop('subject')
    
        subject: dict = SubjectModel.query.filter_by(subject=subject_name).first()
        
        check_subject_existing(subject, subject_name)
        
        data['subject_id'] = subject.id
        data['student_id'] = student.get('id')
        
        registration = StudentSubjectModel(**data)
        
        current_app.db.session.add(registration)
        current_app.db.session.commit()
    
    except (
        InvalidKeySubjectRegisterError, 
        InvalidTypeSubjectRegisterError
        ) as error:
        return jsonify(error.message), 400
    
    except SubjectNotFoundError as error:
        return jsonify(error.message), 404
    
    return jsonify(
        {
			'message': f"subject '{subject_name}' successfully registered!"
		}
        ), 201