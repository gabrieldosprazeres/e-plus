from flask import current_app
from app.excepetions.login_exception import IncorrectPasswordError, InvalidKeyLoginError, InvalidTypeLoginError, EmailNotFoundError
from app.excepetions.subject_exception import InvalidKeySubjectError, InvalidTypeSubjectError, SubjectAlreadyExistsError
from app.models.address_model import AddressModel
from app.models.subject_model import SubjectModel
from app.excepetions.phone_exception import InvalidKeyPhoneError, InvalidTypePhoneError
from app.excepetions import EmailAlreadyExistsError
from app.excepetions.student_exception import InvalidKeyStudentError, InvalidTypeStudentError


# Student Functions

def check_key_for_student(data: dict):
    
    keys = ['name', 'last_name', 'age', 'grade', 'email', 'password', 'state', 'city', 'district', 'street', 'house_number', 'complement']
    
    for key in data.keys():
        if not key in keys or len(data) < 12:
            raise InvalidKeyStudentError(**data)


def check_email(data: dict, model):

    email = model.query.filter_by(email=data.get('email')).first()

    if email:
        raise EmailAlreadyExistsError(data.get('email'))


def check_type_for_student(data: dict):
    
    name = data.get('name')
    last_name = data.get('last_name')
    age = data.get('age')
    grade = data.get('grade')
    email = data.get('email')
    password = data.get('password')
    state = data.get('state')
    city = data.get('city')
    district = data.get('district')
    street = data.get('street')
    house_number = data.get('house_number')
    complement = data.get('complement')
    
    if type(name) != str or type(last_name) != str or type(age) != int or type(grade) != str or type(email) != str or type(password) != str or type(state) != str or type(city) != str or type(district) != str or type(street) != str or type(house_number) != str or type(complement) != str:
        raise InvalidTypeStudentError(**data)


def format_address(data: dict):
    
    state = data.pop('state')
    city = data.pop('city')
    district = data.pop('district')
    street = data.pop('street')
    house_number = data.pop('house_number')
    complement = data.pop('complement')
    
    address = {
        'state': state,
        'city': city,
        'district': district,
        'street': street,
        'house_number': house_number,
        'complement': complement
    }
    
    return address


def adding_address(address, student_id):

    address['student_id'] = student_id

    adding_address = AddressModel(**address)

    current_app.db.session.add(adding_address)

    current_app.db.session.commit()


# Phone Functions

def check_key_for_phone(data: dict):
    
    keys = ['name', 'phone_number']
    
    for key in data.keys():
        if not key in keys or len(data) < 2:
            raise InvalidKeyPhoneError(**data)


def check_type_for_phone(data: dict):
    
    name = data.get('name')
    phone_number = data.get('phone_number')
    
    if type(name) != str or type(phone_number) != str:
        raise InvalidTypePhoneError(**data)


# Subject Functions

def check_subject(data: dict):

    subject = SubjectModel.query.filter_by(subject=data.get('subject')).first()

    if subject:
        raise SubjectAlreadyExistsError(data.get('subject'))


def check_key_for_subject(data: dict):
    
    if not 'subject' in data.keys() or len(data) > 1:
        raise InvalidKeySubjectError(data.get('subject'))


def check_type_for_subject(data: dict):
    
    subject = data.get('subject')
    
    if type(subject) != str:
        raise InvalidTypeSubjectError(subject)


# Signin Functions

def check_key_for_login(data: dict):
    
    keys = ['email', 'password']
    
    for key in data.keys():
        if not key in keys or len(data) < 2:
            raise InvalidKeyLoginError(**data)


def check_type_for_login(data: dict):
    
    email = data.get('email')
    password = data.get('password')
    
    if type(email) != str or type(password) != str:
        raise InvalidTypeLoginError(**data)


def check_password(user: list, data: dict):

    if not user.check_password(data.get('password')):
        raise IncorrectPasswordError()


def check_email_existing(user: list, data: dict):

    if not user:
        raise EmailNotFoundError(data.get('email'))