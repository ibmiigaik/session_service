from flask import Blueprint
from flask import current_app as app
from flask import request, render_template, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from session_service.models import User
from session_service.utils import user as current_user
from session_service.utils.helpers import redirect_url, get_errors, \
    create_session, clear_session
from session_service.utils.user import get_current_user

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    errors = get_errors()

    if current_user.authorized():
        return redirect(redirect_url())

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = generate_password_hash(
            request.form.get("password", "")).strip()
        first_name = request.form.get("first_name", "").strip()
        last_name = request.form.get("last_name", "").strip()
        patronymic = request.form.get("patronymic", "").strip()
        addmission_year = request.form.get("addmission_year", "").strip()
        direction = request.form.get("direction", "").strip()
        group_num = request.form.get("group_num", "").strip()

        user = User.objects(username=username).first()

        if user:
            errors.append("That username already exists")

        if len(errors) > 0:
            return render_template(
                "register.html",
                errors=errors,
                username=request.form["login"],
                password=request.form["password"],
                first_name=request.form['first_name'],
                last_name=request.form['last_name'],
                patronymic=request.form['patronymic'],
                addmission_year=request.form['addmission_year'],
                direction=request.form['direction'],
                group_num=request.form['group_num']
            )

        with app.app_context():
            user = User(username=username, password=password,
                        first_name=first_name, last_name=last_name,
                        patronymic=patronymic, addmission_year=addmission_year,
                        direction=direction,
                        group_num=group_num, role="student")
            user.save()

            return redirect(url_for("auth.login"))

    return render_template("register.html", errors=errors)


@auth.route("/login", methods=["POST", "GET"])
def login():
    errors = get_errors()

    if current_user.authorized():
        return redirect(url_for("auth.user_info"))

    if request.method == "POST":
        username = request.form["login"]
        password = request.form["password"]

        user = User.objects(username=username).first()

        if user and check_password_hash(user.password, password):
            create_session(user)
            return redirect(url_for("auth.user_info"))

        errors.append("Username or password incorrect")

    return render_template("login.html", errors=errors)


@auth.route("/user_info", methods=["GET"])
def user_info():
    if current_user.authorized():
        user = get_current_user()
        return render_template('user_info.html', username=user.username,
                               user_role=user.role,
                               first_name=user.first_name,
                               last_name=user.last_name,
                               patronymic=user.patronymic,
                               addmission_year=user.addmission_year,
                               direction=user.direction,
                               group_num=user.group_num)
      return redirect(url_for('auth.login'))


@auth.route("/logout", methods=["GET"])
def logout():
    if current_user.authorized():
        clear_session()

    return redirect(redirect_url("auth.login"))
