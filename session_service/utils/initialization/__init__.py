from session_service.utils import user as current_user


def init_template_globals(app):
    app.jinja_env.globals['authorized'] = current_user.authorized
