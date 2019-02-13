# from app import app
#
#
# @app.route('/')
# @app.route('/index')
# def index():
#     user = {'username': 'Miguel'}
#     return '''
# <html>
#     <head>
#         <title>Home Page - Microblog</title>
#     </head>
#     <body>
#         <h1>Hello, ''' + user['username'] + '''!</h1>
#         <input type="text" /> <!-- This is for text input -->
#         <input type="file" /> <!-- This is for uploading files -->
#         <input type="checkbox" /> <!-- This is for checkboxes -->
#     </body>
# </html>'''

from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def test():
    res = 'The method of your request is [%s], and your arguments are %s'
    return res % (request.method, request.args)


@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)      # 采用index.html的模板


@app.route('/login', methods=['GET', 'POST'])   # 设置允许post提交方式
def login():
    form = LoginForm()
    if form.validate_on_submit():   # 执行form校验，get请求返回false会使得跳过if
        flash('Login requested for user {}, remember_me={}'.format(     # flash()函数是向用户显示消息的有效途径
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))       # 重定向到它的参数所关联的URL
    return render_template('login.html', title='Sign In', form=form)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    
