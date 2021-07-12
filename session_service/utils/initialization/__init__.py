from session_service.utils import user as current_user

def init_template_globals(app):
    app.jinja_env.globals['authed'] = current_user.authed