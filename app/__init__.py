from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register blueprints, routes are handled in a different file
    from .routes import main
    app.register_blueprint(main)

    return app