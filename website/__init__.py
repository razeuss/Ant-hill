from flask import Flask


def create_app():
    app = Flask(__name__)
    
    from .main_route import views
    app.register_blueprint(views)
    
    return app