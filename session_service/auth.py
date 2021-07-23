from flask import current_app as app
from flask import Blueprint, session
from flask import request, get_flashed_messages, render_template, redirect, url_for

from session_service.models import User, Table
from session_service.utils import user as current_user
from session_service.utils.user import get_current_user
from session_service.utils.helpers import redirect_url, get_errors, create_session, clear_session

from werkzeug.security import generate_password_hash, check_password_hash


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():

    errors = get_errors()

    if current_user.authed():
        return redirect(redirect_url())

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = generate_password_hash(request.form.get("password", "")).strip()
        first_name = request.form.get("first_name","").strip()
        last_name = request.form.get("last_name","").strip()
        patronymic = request.form.get("patronymic","").strip()
        addmission_year = request.form.get("addmission_year", "").strip()
        direction = request.form.get("direction","").strip()
        group_num = request.form.get("group_num", "").strip()

        user = User.objects(username=username).first()

        if user:
            errors.append("That username already exists")

        if len(errors) > 0:
            return render_template(
                "register.html",
                errors=errors,
                username=request.form["username"],
                password=request.form["password"],
                first_name = request.form['first_name'],
                last_name = request.form['last_name'],
                patronymic = request.form['patronymic'],
                addmission_year = request.form['addmission_year'],
                direction = request.form['direction'],
                group_num = request.form['group_num']
            )

        with app.app_context():
            user = User(username = username, password = password, first_name = first_name, last_name = last_name, patronymic = patronymic, addmission_year = addmission_year, direction = direction, group_num = group_num, role="student")
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

        if user and check_password_hash(user.password, password):
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
        check = user.direction + user.group_num + user.addmission_year
        table = Table.objects(check=check).first()
        if table:
            return render_template('user_info.html', username=user.username, user_role=user.role, first_name = user.first_name, last_name = user.last_name, patronymic = user.patronymic, addmission_year = user.addmission_year, direction = user.direction, group_num = user.group_num, monday = table.monday, tuesday = table.tuesday, wednesday = table.wednesday, thursday = table.thursday, friday = table.friday, saturday = table.saturday, m_1_u = table.m_1_u, m_2_u = table.m_2_u, m_3_u = table.m_3_u, m_4_u = table.m_4_u, m_5_u = table.m_5_u, m_6_u = table.m_6_u, m_7_u = table.m_7_u, m_1_d = table.m_1_d, m_2_d = table.m_2_d, m_3_d = table.m_3_d, m_4_d = table.m_4_d, m_5_d = table.m_5_d, m_6_d = table.m_6_d, m_7_d = table.m_7_d, t_1_u = table.t_1_u, t_2_u = table.t_2_u, t_3_u = table.t_3_u, t_4_u = table.t_4_u, t_5_u = table.t_5_u, t_6_u = table.t_6_u, t_7_u = table.t_7_u, t_1_d = table.t_1_d, t_2_d = table.t_2_d, t_3_d = table.t_3_d, t_4_d = table.t_4_d, t_5_d = table.t_5_d,  t_6_d = table.t_6_d, t_7_d = table.t_7_d, w_1_u = table.w_1_u, w_2_u = table.w_2_u, w_3_u = table.w_3_u, w_4_u = table.w_4_u, w_5_u = table.w_5_u, w_6_u = table.w_6_u, w_7_u = table.w_7_u, w_1_d = table.w_1_d, w_2_d = table.w_1_d, w_3_d = table.w_1_d, w_4_d = table.w_1_d, w_5_d = table.w_1_d, w_6_d = table.w_1_d, w_7_d = table.w_1_d, th_1_u = table.th_1_u, th_2_u = table.th_2_u, th_3_u = table.th_3_u, th_4_u = table.th_4_u, th_5_u = table.th_5_u, th_6_u = table.th_6_u, th_7_u = table.th_7_u, th_1_d = table.th_1_d, th_2_d = table.th_2_d, th_3_d = table.th_3_d, th_4_d = table.th_4_d, th_5_d = table.th_5_d, th_6_d = table.th_6_d, th_7_d = table.th_7_d, f_1_u = table.f_1_u, f_2_u = table.f_2_u, f_3_u = table.f_3_u, f_4_u = table.f_4_u, f_5_u = table.f_5_u, f_6_u = table.f_6_u, f_7_u = table.f_7_u, f_1_d = table.f_1_d, f_2_d = table.f_2_d, f_3_d = table.f_3_d, f_4_d = table.f_4_d, f_5_d = table.f_5_d, f_6_d = table.f_6_d, f_7_d = table.f_7_d, s_1_u = table.s_1_u, s_2_u = table.s_2_u, s_3_u = table.s_3_u, s_4_u = table.s_4_u, s_5_u = table.s_5_u, s_6_u = table.s_6_u, s_7_u = table.s_7_u, s_1_d = table.s_1_d, s_2_d = table.s_2_d, s_3_d = table.s_3_d, s_4_d = table.s_4_d, s_5_d = table.s_5_d, s_6_d = table.s_6_d, s_7_d = table.s_7_d)
        else:
            return render_template('user_info.html', username=user.username, user_role=user.role, first_name = user.first_name, last_name = user.last_name, patronymic = user.patronymic, addmission_year = user.addmission_year, direction = user.direction, group_num = user.group_num)

    else:
        return redirect(url_for('auth.login'))


@auth.route('/logout', methods=['GET'])
def logout():

    if current_user.authed():
        clear_session()

    return redirect(redirect_url('auth.login'))
