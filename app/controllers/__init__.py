# from app.excepetions import PhoneAlreadyExistsError
from app.excepetions.student_exception import InvalidKeyStudentError, InvalidTypeStudentError


def check_key_for_student(data: dict):
    
    keys = ['name', 'last_name', 'age', 'grade', 'email', 'password']
    
    for key in data.keys():
        if not key in keys or len(data) < 6:
            raise InvalidKeyStudentError(**data)


# def check_phone(data: dict, model):

#     phone = model.query.filter_by(phone=data.get('phone')).first()

#     if phone:
#         raise PhoneAlreadyExistsError(data.get('phone'))


def check_type_for_student(data: dict):
    
    name = data.get('name')
    last_name = data.get('last_name')
    age = data.get('age')
    grade = data.get('grade')
    email = data.get('email')
    password = data.get('password')
    
    if type(name) != str or type(last_name) != str or type(age) != int or type(grade) != str or type(email) != str or type(password) != str:
        raise InvalidTypeStudentError(**data)