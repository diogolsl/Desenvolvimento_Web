from flask import Flask 
app = Flask(__name__)
def create_app():

    from .blueprints.pages import bp as pages_bp
    app.register_blueprint(pages_bp)


    return app
