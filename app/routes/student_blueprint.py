from flask import Blueprint
from app.controllers.student_controller import deleting_student, get_all_students, get_info_student, registering_student, updating_address, updating_student, get_filter_by_id
from app.controllers.phone_controller import creating_phone_number, deleting_phone, updating_phone
from app.controllers.login_controller import signin_student
from flask_jwt_extended import jwt_required

bp_student = Blueprint('bp_student', __name__, url_prefix='/students')

bp_student.get('')(get_all_students)
bp_student.get('/student/<int:student_id>')(get_filter_by_id)
bp_student.get('/student')(jwt_required()(get_info_student))
bp_student.post('/student/signup')(registering_student)
bp_student.post('/phone')(jwt_required()(creating_phone_number))
bp_student.post('/student/signin')(signin_student)
bp_student.patch('/phone/updating/<int:phone_id>')(jwt_required()(updating_phone))
bp_student.patch('/student/updating')(jwt_required()(updating_student))
bp_student.patch('/student/address/updating')(jwt_required()(updating_address))
bp_student.delete('/phone/deleting/<int:phone_id>')(jwt_required()(deleting_phone))
bp_student.delete('/student/deleting')(jwt_required()(deleting_student))