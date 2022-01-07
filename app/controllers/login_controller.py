from flask import request, jsonify
from flask_jwt_extended import create_access_token
from app.controllers import check_email_existing, check_key_for_login, check_password, check_type_for_login
from app.models.student_model import StudentModel
from app.excepetions.login_exception import EmailNotFoundError, IncorrectPasswordError, InvalidKeyLoginError, InvalidTypeLoginError


def signin_student():

    data: dict = request.get_json()

    try:
        check_key_for_login(data)
        check_type_for_login(data)

        student = StudentModel.query.filter_by(email=data.get('email')).first()

        check_email_existing(student, data)
        check_password(student, data)

        access_token = create_access_token(student)

    except (
        InvalidKeyLoginError, 
        InvalidTypeLoginError
        ) as error:
        return jsonify(error.message), 400

    except IncorrectPasswordError as error:
        return jsonify(error.message), 401

    except EmailNotFoundError as error:
        return jsonify(error.message), 404

    return {"access_token": access_token}, 200