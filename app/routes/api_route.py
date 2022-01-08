from flask import Blueprint, render_template
from app.routes.student_blueprint import bp_student
from app.routes.subject_blueprint import bp_subject


def index():
    return render_template('index.html')


bp_api = Blueprint('bp_api', __name__, url_prefix='/api')

bp_api.get('')(index)
bp_api.register_blueprint(bp_student)
bp_api.register_blueprint(bp_subject)