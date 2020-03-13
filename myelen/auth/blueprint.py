from flask import Blueprint


bp = Blueprint('auth', __name__, template_folder='templates')

@bp.route('/login')
def index():
    return 'OK1'
