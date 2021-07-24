from flask import request, url_for, get_flashed_messages
from flask import session


def redirect_url(default=''):
    return request.args.get('next') or request.referrer or url_for(default)


def create_session(user):
    session['user_id'] = user.id
    session['username'] = user.username
    session['role'] = user.role


def clear_session():
    session.clear()


def get_errors():
    return get_flashed_messages(category_filter=request.endpoint + ".errors")
