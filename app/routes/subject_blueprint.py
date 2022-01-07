from flask import Blueprint
from app.controllers.subject_controller import creating_subject


bp_subject = Blueprint('bp_subject', __name__, url_prefix='/subjects')


bp_subject.post('')(creating_subject)