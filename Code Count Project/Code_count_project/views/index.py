from flask import Blueprint, session, redirect, render_template, request
from ..utils.DbClient import fetch_all, fetch_one, insert
import os
from settings import Config
from uuid import uuid4

ind = Blueprint('ind', __name__)


# 蓝图中所有请求访问前都先检查是否登录
@ind.before_request
def process_request():
    if not session.get('user_info'):
        return redirect('/login')


@ind.route('/home')
def index():
    return render_template('index.html')


@ind.route('/user_list')
def user_list():
    sql = 'select id, user, nickname from userinfo'
    data_list = fetch_all(sql, [])
    return render_template('user_list.html', data_list=data_list)


@ind.route('/detail/<int:nid>')
def detail(nid):
    sql = 'select id, line, ctime from record where user_id =?'
    data_list = fetch_all(sql, (nid,))
    return render_template('detail.html', data_list=data_list)


@ind.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    file_obj = request.files.get('code')
    target_path = os.path.join(Config.FILE_PATH, str(uuid4()))

    if not file_obj.filename.endswith('.zip'):
        return '请上传压缩文件'
    import shutil
    shutil._unpack_zipfile(file_obj, target_path)
    total_sum = 0
    for _path, _folder, file_list in os.walk(target_path):
        for file in file_list:
            file_path = os.path.join(_path, file)
            if file.endswith('.py'):
                total_sum += sum(1 for line in open(file_path, 'r', encoding='utf-8') if line.strip())

    import datetime
    ctime = (datetime.datetime.today()).strftime('%Y%m%d')
    sql = 'select * from record where user_id=? and ctime=?'
    data = fetch_one(sql, (session['user_info']['id'], ctime))
    if data:
        return '你今天已经上传了代码'
    sql = 'insert into record(line, ctime, user_id)values(?, ?, ?)'
    insert(sql, (total_sum, ctime, session['user_info']['id']))
    return '上传了%s行代码' % total_sum
