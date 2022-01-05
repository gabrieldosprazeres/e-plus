from flask import Blueprint
from app.controllers.student_controller import get_all_students, registering_student


bp_student = Blueprint('bp_student', __name__, url_prefix='/students')


bp_student.get('')(get_all_students)
bp_student.post('')(registering_student)