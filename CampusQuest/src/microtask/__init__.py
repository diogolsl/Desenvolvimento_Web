from flask import Flask 
from flask import render_template

def create_app():
    app = Flask(__name__)

    from .blueprints.pages import bp as pages_bp
    app.register_blueprint(pages_bp)

    from .blueprints.missions import bp as missions_bp
    app.register_blueprint(missions_bp)

    from .blueprints.notices import bp as notices_bp
    app.register_blueprint(notices_bp)

    from .blueprints.greet import bp as greet_bp
    app.register_blueprint(greet_bp)

    app.errorhandler(404)(lambda e: (render_template('errors/404.html'), 404))

    return app
