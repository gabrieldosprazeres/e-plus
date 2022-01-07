from flask import request, jsonify, current_app
from flask_jwt_extended import get_jwt_identity
from app.models.address_model import AddressModel
from app.models.student_model import StudentModel
from app.excepetions import EmailAlreadyExistsError, PatternEmailError
from app.excepetions.student_exception import InvalidKeyStudentError, InvalidKeyUpdatingAddressError, InvalidKeyUpdatingError, InvalidTypeStudentError, InvalidTypeUpdatingError, InvalidTypeUpdatingAddressError
from app.controllers import adding_address, check_email, check_email_pattern, check_key_for_address, check_key_for_student, check_key_for_updating, check_type_for_address, check_type_for_student, check_type_for_updating, format_address, updating_password


def get_all_students():

    students = StudentModel.query.all()

    return jsonify(
        [
            {
                'id': student.id,
                'name': student.name,
                'last_name': student.last_name,
                'age': student.age,
                'grade': student.grade,
                'email': student.email,
                'address': student.address,
                'phones': student.phones,
                'subjects': student.subjects
            } for student in students
        ]
        ), 200
    

def get_info_student():
    
    student: dict = get_jwt_identity()
    
    info_student = StudentModel.query.get(student.get('id'))
    
    return jsonify(
        [
            {
                'id': info_student.id,
                'name': info_student.name,
                'last_name': info_student.last_name,
                'age': info_student.age,
                'grade': info_student.grade,
                'email': info_student.email,
                'address': info_student.address,
                'phones': info_student.phones,
                'subjects': info_student.subjects
            }
        ]
        ), 200


def registering_student():
    data: dict = request.get_json()

    try:
        check_key_for_student(data)
        check_type_for_student(data)
        check_email(data, StudentModel)
        check_email_pattern(data)
        
        address = format_address(data)
        
        password_to_hash = data.pop('password')

        student = StudentModel(**data)
        
        student.password = password_to_hash

        current_app.db.session.add(student)
        
        current_app.db.session.commit()
        
        adding_address(address, student.id)

    except (
        InvalidKeyStudentError, 
        InvalidTypeStudentError,
        PatternEmailError
        ) as error:
        return jsonify(error.message), 400

    except EmailAlreadyExistsError as error:
        return jsonify(error.message), 409

    return jsonify(student), 201



def updating_student():
    data: dict = request.get_json()
    student: dict = get_jwt_identity()
    
    try:
        check_key_for_updating(data)
        check_type_for_updating(data)
        check_email(data, StudentModel)
        check_email_pattern(data)
        updating_password(data)
        
        StudentModel.query.filter_by(id=student.get('id')).update(data)
        
        current_app.db.session.commit()

    except (
        InvalidKeyUpdatingError,
        InvalidTypeUpdatingError,
        PatternEmailError
        ) as error:
        return jsonify(error.message), 400

    except EmailAlreadyExistsError as error:
        return jsonify(error.message), 409
    
    return "", 204


def updating_address():
    data: dict = request.get_json()
    student: dict = get_jwt_identity()

    try:
        check_key_for_address(data)
        check_type_for_address(data)

        AddressModel.query.filter_by(student_id=student.get('id')).update(data)
        current_app.db.session.commit()

    except (
        InvalidKeyUpdatingAddressError, 
        InvalidTypeUpdatingAddressError
        ) as error:
        return jsonify(error.message), 400

    return "", 204


def deleting_student():
    
    student: dict = get_jwt_identity()
    
    StudentModel.query.filter_by(id=student.get('id')).delete()

    current_app.db.session.commit()
    
    return "", 204
