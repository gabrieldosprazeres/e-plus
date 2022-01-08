from flask import Blueprint
from app.controllers.student_controller import deleting_student, get_all_students, get_info_student, registering_student, updating_address, updating_student, get_filter_by_id
from app.controllers.phone_controller import creating_phone_number, deleting_phone, updating_phone
from app.controllers.login_controller import signin_student
from flask_jwt_extended import jwt_required

bp_student = Blueprint('bp_student', __name__, url_prefix='/students')
																							# Student CRUD
bp_student.get('')(get_all_students)														# List all registered students
bp_student.get('/student')(jwt_required()(get_info_student))								# Lists the information of the student who is logged in (token required)
bp_student.get('/student/<int:student_id>')(get_filter_by_id)								# Filters a student by their ID
bp_student.post('/student/signup')(registering_student)										# Register a student on the API
bp_student.post('/student/signin')(signin_student)											# Login to the API
bp_student.patch('/student/updating')(jwt_required()(updating_student))						# Update student data in API
bp_student.patch('/student/address/updating')(jwt_required()(updating_address))				# Update student address data in API
bp_student.delete('/student/deleting')(jwt_required()(deleting_student))					# Delete a student from the API
bp_student.post('/student/phone')(jwt_required()(creating_phone_number))					# Register a phone number for the student
bp_student.patch('/student/phone/updating/<int:phone_id>')(jwt_required()(updating_phone))	# Update a phone number on the student
bp_student.delete('/student/phone/deleting/<int:phone_id>')(jwt_required()(deleting_phone))	# Deletes a phone number on the student