from flask import session

from session_service.models import User


def get_current_user():
    if authed:
        user = User.objects(id=session['user_id']).first()

        return user

    else:
        return None

def authed():
    return bool(session.get('user_id', False))