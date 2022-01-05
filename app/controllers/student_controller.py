from flask import request, jsonify, current_app
from app.controllers import check_key_for_student, check_phone, check_type_for_student
from app.excepetions import PhoneAlreadyExistsError
from app.excepetions.student_exception import InvalidKeyStudentError, InvalidTypeStudentError
from app.models.student_model import StudentModel


def get_all_students():

    students = StudentModel.query.all()

    return jsonify(students), 200


def registering_student():
    data = request.get_json()

    try:
        check_key_for_student(data)
        check_phone(data, StudentModel)
        check_type_for_student(data)
        student = StudentModel(**data)

        current_app.db.session.add(student)
        current_app.db.session.commit()

    except (
        InvalidKeyStudentError, 
        InvalidTypeStudentError
        ) as error:
        return jsonify(error.message), 400

    except PhoneAlreadyExistsError as error:
        return jsonify(error.message), 409

    return jsonify(student), 201
