from myelen.auth.blueprint import bp


@bp.route('/login')
def index():
    return 'OK1'
