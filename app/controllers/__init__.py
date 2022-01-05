from app.excepetions import PhoneAlreadyExistsError
from app.excepetions.student_exception import InvalidKeyStudentError, InvalidTypeStudentError


def check_key_for_student(data: dict):
    
    keys = ['full_name', 'age', 'phone']
    
    for key in data.keys():
        if not key in keys or len(data) < 3:
            raise InvalidKeyStudentError(**data)


def check_phone(data: dict, model):

    phone = model.query.filter_by(phone=data.get('phone')).first()

    if phone:
        raise PhoneAlreadyExistsError(data.get('phone'))


def check_type_for_student(data: dict):
    
    full_name = data.get('full_name')
    age = data.get('age')
    phone = data.get('phone')
    
    if type(full_name) != str or type(age) != int or type(phone) != str:
        raise InvalidTypeStudentError(**data)