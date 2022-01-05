from flask import Blueprint
from app.routes.student_blueprint import bp_student


bp_api = Blueprint('bp_api', __name__, url_prefix='/api')

bp_api.register_blueprint(bp_student)