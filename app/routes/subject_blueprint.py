from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.subject_controller import creating_subject, get_subject_by_id
from app.controllers.student_subject_controller import student_registration_subject

bp_subject = Blueprint('bp_subject', __name__, url_prefix='/subjects')

bp_subject.get('/get_subject_by_id/<int:subject_id>')(get_subject_by_id)
bp_subject.post('')(creating_subject)
bp_subject.post('/registration')(jwt_required()(student_registration_subject))