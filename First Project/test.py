from flask import Flask, render_template, request, redirect, session, url_for, make_response

app = Flask(__name__)
app.secret_key = 'aa'


@app.route('/<int:nid>', methods=['GET', 'POST'])
def index(nid):
    print(url_for('index', nid=nid))
    obj = make_response(str(nid))
    obj.headers['xxx'] = 1234
    obj.set_cookie('key', 'ss1234')
    return obj


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login_test.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'yang' and pwd == 'syss':
            session['user'] = user
            return redirect('/')
        else:
            return render_template('login_test.html', errors='密码错了')


if __name__ == '__main__':
    app.run()
