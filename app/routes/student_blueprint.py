from flask import Blueprint
from app.controllers.student_controller import registering_student


bp_student = Blueprint('bp_student', __name__, url_prefix='/student')

bp_student.post('')(registering_student)