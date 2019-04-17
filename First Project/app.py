from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.config.from_object('settings.DevConfig')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    user = request.form.get('user')
    pwd = request.form.get('pwd')
    if user == 'yang' and pwd == 'syss':
        session['user'] = user
        return redirect('/index')
    return render_template('login.html', error='用户名或密码错误')


@app.route('/index')
def index():
    user = session.get('user')
    if not user:
        return redirect('/login')

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
