from flask import Blueprint
from app.controllers.student_controller import get_all_students, registering_student
from app.controllers.phone_controller import creating_phone_number
from app.controllers.login_controller import signin_student


bp_student = Blueprint('bp_student', __name__, url_prefix='/students')


bp_student.get('')(get_all_students)
bp_student.post('')(registering_student)
bp_student.post('/phone/<int:student_id>')(creating_phone_number)
bp_student.post('/signin')(signin_student)