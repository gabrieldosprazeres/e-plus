from flask import request, jsonify, current_app
from app.controllers import check_key_for_subject, check_subject, check_type_for_subject
from app.excepetions.subject_exception import InvalidKeySubjectError, InvalidTypeSubjectError, SubjectAlreadyExistsError
from app.models.subject_model import SubjectModel


def creating_subject():
    data = request.get_json()
    
    try:
        check_key_for_subject(data)
        check_type_for_subject(data)
        check_subject(data)

        subject = SubjectModel(**data)
    
        current_app.db.session.add(subject)
        current_app.db.session.commit()

    except (
        InvalidKeySubjectError, 
        InvalidTypeSubjectError
        ) as error:
        return jsonify(error.message), 400
    
    except SubjectAlreadyExistsError as error:
        return jsonify(error.message), 409
    
    return jsonify(subject), 201