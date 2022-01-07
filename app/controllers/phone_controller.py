from flask import request, jsonify, current_app
from app.controllers import check_key_for_phone, check_type_for_phone
from app.excepetions.phone_exception import InvalidKeyPhoneError, InvalidTypePhoneError
from app.models.phone_model import PhoneModel


def creating_phone_number(student_id: int):
    data = request.get_json()
    
    try:
        check_key_for_phone(data)
        check_type_for_phone(data)

        data['student_id'] = student_id
    
        phone = PhoneModel(**data)
        
        current_app.db.session.add(phone)
        current_app.db.session.commit()
    except (
        InvalidKeyPhoneError, 
        InvalidTypePhoneError
        ) as error:
        return jsonify(error.message), 400
    
    return jsonify(phone), 200