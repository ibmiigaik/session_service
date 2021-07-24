from flask import session

from session_service.models import User


def get_current_user():
    if authorized():
        return User.objects(id=session['user_id']).first()


def authorized():
    return bool(session.get('user_id', False))
