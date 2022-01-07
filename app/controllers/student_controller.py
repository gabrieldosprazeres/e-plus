from flask import request, jsonify, current_app
from app.controllers import adding_address, check_email, check_key_for_student, check_type_for_student, format_address
from app.excepetions import EmailAlreadyExistsError
from app.excepetions.student_exception import InvalidKeyStudentError, InvalidTypeStudentError
from app.models.student_model import StudentModel


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
                'phones': student.phones
            } for student in students
        ]
        ), 200


def registering_student():
    data: dict = request.get_json()

    try:
        check_key_for_student(data)
        check_type_for_student(data)
        check_email(data, StudentModel)
        
        address = format_address(data)
        
        password_to_hash = data.pop('password')

        student = StudentModel(**data)
        
        student.password = password_to_hash

        current_app.db.session.add(student)
        
        current_app.db.session.commit()
        
        adding_address(address, student.id)

    except (
        InvalidKeyStudentError, 
        InvalidTypeStudentError
        ) as error:
        return jsonify(error.message), 400

    except EmailAlreadyExistsError as error:
        return jsonify(error.message), 409

    return jsonify(student), 201
