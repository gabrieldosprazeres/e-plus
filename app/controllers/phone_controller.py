from flask import request, jsonify, current_app
from flask_jwt_extended import get_jwt_identity
from app.controllers import check_and_deleting_phone, check_and_updating_phone, check_key_for_phone, check_phone_id, check_phone_pattern, check_type_for_phone
from app.excepetions import PatternPhoneError
from app.excepetions.phone_exception import InvalidKeyPhoneError, InvalidTypePhoneError, InvalidAccessPhoneError, PhoneIdNotFoundError
from app.models.phone_model import PhoneModel
from app.models.student_model import StudentModel


def creating_phone_number():
    data = request.get_json()
    student: dict = get_jwt_identity()

    try:
        check_key_for_phone(data)
        check_type_for_phone(data)
        check_phone_pattern(data)

        data['student_id'] = student.get('id')

        phone = PhoneModel(**data)

        current_app.db.session.add(phone)
        current_app.db.session.commit()

    except (
        InvalidKeyPhoneError, 
        InvalidTypePhoneError,
        PatternPhoneError
        ) as error:
        return jsonify(error.message), 400

    return jsonify(phone), 200


def updating_phone(phone_id: int):
    data: dict = request.get_json()
    student: dict = get_jwt_identity()

    try:
        check_phone_id(phone_id, PhoneModel)

        info_student = StudentModel.query.get(student.get('id'))

        phone = PhoneModel.query.filter_by(id=phone_id).first()

        check_and_updating_phone(info_student, phone, phone_id, data, PhoneModel)

    except InvalidAccessPhoneError as error:
        return jsonify(error.message), 401
    
    except PhoneIdNotFoundError as error:
        return jsonify(error.message), 404

    return "", 204


def deleting_phone(phone_id: int):
    student = get_jwt_identity()

    try:
        check_phone_id(phone_id, PhoneModel)

        info_student = StudentModel.query.get(student.get('id'))

        phone = PhoneModel.query.filter_by(id=phone_id).first()

        check_and_deleting_phone(info_student, phone, phone_id, PhoneModel)

    except InvalidAccessPhoneError as error:
        return jsonify(error.message), 401
    
    except PhoneIdNotFoundError as error:
        return jsonify(error.message), 404
    
    return "", 204