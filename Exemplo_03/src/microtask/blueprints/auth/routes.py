from . import bp

@bp.route('/login')
def login():
    return "Login Page"