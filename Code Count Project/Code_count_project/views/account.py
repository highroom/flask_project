from flask import Blueprint, render_template, request, session, redirect
from ..utils import DbClient
from ..utils.md5 import md5

account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('user')
    password = request.form.get('pwd')

    pwd_md5 = md5(password)

    sql = "select id, nickname from userinfo where user=? and pwd = ?"
    data = DbClient.fetch_one(sql, (username, pwd_md5))

    if not data:
        return render_template('login.html', error='用户名密码错')

    session['user_info'] = data

    return redirect('/home')


@account.route('/logout')
def logout():
    if 'user_info' in session:
        del session['user_info']
    return redirect('/login')
