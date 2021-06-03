import pymysql

from flask import Blueprint, url_for, render_template, flash, request, session, g
from werkzeug.security import check_password_hash
from werkzeug.utils import redirect

from policy import db
from policy.forms import UserCreateForm, UserLoginForm
# from policy.models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

def create_connection():
    db_database ="login"
    db_name ="admin"
    db_password ="wqend1001"
    db_url = "mybide.cutyxjtrt78p.us-east-1.rds.amazonaws.com"

    conn = pymysql.connect(host = db_url, user = db_name, passwd = db_password, db = db_database, port = 3306)
    cursor = conn.cursor()

    return conn, cursor


@bp.route('/login/', methods=('GET', 'POST'))
def login():
    form = UserLoginForm()

    if request.method == 'POST' and form.validate_on_submit():
        conn, cursor = create_connection()

        sql = "select * from output_users where id = %s"
        cursor.execute(sql, form.username.data)
        check_validate = cursor.fetchall()
        print(check_validate)
        print(type(check_validate))

        if len(check_validate) == 0:
            print("error!!!")
            error = "존재하지 않는 사용자!!"
            flash(error)
        elif check_validate[0][1] != form.password.data:
            error = "잘못된 비밀번호 입니다!!"
            flash(error)
        else:
            print("good!!!")
            session.clear()
            session['user_id'] = form.username.data
            # return render_template('auth/signup.html')

            return redirect(url_for('main.index'))

    return render_template('auth/login.html', form=form)

@bp.before_app_request
def load_logged_in_user():
    user_id = [session.get('user_id')]

    conn, cursor = create_connection()
    sql = "select * from output_users where id=%s"
    cursor.execute(sql, user_id)
    id_temp = cursor.fetchall()

    if user_id is None:
        g.user = None
    else:
        g.user = id_temp

@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index')) # 수정

    
@bp.route('/signup/', methods=('GET', 'POST'))
def signup():

    form = UserCreateForm()
    conn, cursor = create_connection()

    # id, pwd, name, age, sex, address, create_date
    if request.method == 'POST' and form.validate_on_submit():
        sql = "select * from output_users where id=%s"
        cursor.execute(sql, form.id.data)
        check_validate = cursor.fetchall()

        if len(check_validate) == 0:
            # pwd = generate_password_hash(form.password1.data)
            temp = (form.id.data, form.password1.data, form.level.data, form.create_date)
            sql = "insert into output_users (id, pwd, lv, created_at ) values (%s,%s,%s,%s)"

            cursor.execute(sql, temp)
            conn.commit()
            return redirect(url_for('main.index'))
        else:
            flash('이미 존재하는 사용자입니다.')

    cursor.close()
    return render_template('auth/signup.html', form=form)

# ------------------------------------------------------
