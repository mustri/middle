from flask import Flask, request,make_response
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.contrib.cache import SimpleCache

from L.Login import cachehave

from flask import flash, redirect, url_for
from L.Account import Account
from L.AccountTable import AccountTable

autologinCache = SimpleCache()   #用于自动登陆的缓存


class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')


app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'  # for example, '3ef6ffg4'


# @app.route('/home')
@app.route('/', methods=['post', 'get'])
def home2():
    return redirect(url_for('login'))


@app.route('/login', methods=['post', 'get'])
def login():

    user = request.cookies.get('userID')
    if cachehave(user,  autologinCache) == True:
        return redirect(url_for('table'))
    else :
        return app.send_static_file('login.html')


@app.route('/logincookie', methods=['post', 'get'])
def giveweb():
    user = request.form.get('user')
    password = request.form.get('password')

    a = Account(user, password)
#   AccountTable().insert_account(a)
    t = AccountTable().login(a)
    if t==2:
        res = app.make_response(redirect('table'))
        res.set_cookie('userID', user)
        autologinCache.set(user, 1, timeout=1 * 60)
        return res


@app.route('/table', methods=['get', 'post'])
def table():
    context = {
        'shift': 'text',
        'starttime': '14:00',
        'arrivetime': '15:00',
        'fare': '100',
        'remainvote': '50'
    }
    return render_template('table.html', **context)
    # return app.send_static_file('table.html')


@app.route('/blank', methods=['get', 'post'])
def blank():
    return app.send_static_file('blank.html')


@app.route('/findshift', methods=['post'])
def shiftinformation():
    context = [{
        'shift': 'success',
        'starttime': '14:00',
        'arrivetime': '15:00',
        'fare': '100',
        'remainvote': '50'
    }]
    return render_template('table.html', **context)


if __name__ == '__main__':
    app.run(port=80, debug=True)
