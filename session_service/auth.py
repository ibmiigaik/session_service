from flask import current_app as app
from flask import Blueprint, session
from flask import request, get_flashed_messages, render_template, redirect, url_for

from session_service.models import User
from session_service.utils import user as current_user
from session_service.utils.user import get_current_user
from session_service.utils.helpers import redirect_url, get_errors, create_session, clear_session


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    errors = get_errors()

    if current_user.authed():
        return redirect(redirect_url())

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        user = User.objects(username=username).first()

        if user:
            errors.append("That username already exists")

        if len(errors) > 0:
            return render_template(
                "register.html",
                errors=errors,
                username=request.form["username"],
                password=request.form["password"],
            )

        with app.app_context():
            user = User(username=username, password=password, role="student")
            user.save()

            return redirect(url_for("auth.login"))

    else:
        return render_template("register.html", errors=errors)


@auth.route("/login", methods=["POST", "GET"])
def login():
    errors = get_errors()

    if current_user.authed():
        return redirect(url_for('auth.user_info'))

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.objects(username=username).first()

        if user and user.password == password:
            create_session(user)
            return redirect(url_for("auth.user_info"))

        else:
            errors.append('Username or password incorrect')

    return render_template("login.html", errors=errors)


@auth.route('/user_info', methods=['GET'])
def user_info():
    errors = get_errors()

    if current_user.authed():
        user = get_current_user()
        
        return render_template('user_info.html', username=user.username, user_role=user.role)

    else:
        return redirect(url_for('auth.login'))


@auth.route('/logout', methods=['GET'])
def logout():

    if current_user.authed():
        clear_session()

    return redirect(redirect_url('auth.login'))
