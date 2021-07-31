from flask import Flask
from flask_session import Session

from session_service.auth import auth
from session_service.models import db, User
from session_service.utils.initialization import init_template_globals


def create_app(config="session_service.config.Config"):
    app = Flask(__name__)

    with app.app_context():
        app.config.from_object(config)

        session = Session()

        db.init_app(app)
        session.init_app(app)

        init_template_globals(app)

        if app.config.get("DEBUG"):
            User.create_mock_users()

        app.register_blueprint(auth)

        return app
