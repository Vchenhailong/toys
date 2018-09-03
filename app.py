#! /bin/python
# coding:utf-8

# request: 请求对象，封装了客户端发出的 HTTP 请求中的内容
# g:处理请求时用作临时存储的对象。每次请求都会重设这个变量
# session: 用户会话，用于存储请求之间需要“记住”的值的词典

from flask import Flask, request, make_response, g, session, redirect, render_template, abort
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s </p>!' % user_agent


@app.route('/user/<name>')
def welcome(name):
    return render_template('user.html', name=name)


@app.route('/rsp_test')
def rsp_test():
    # 返回一个 response 对象
    rsp = make_response('it works')
    return rsp


@app.route('/logout')
def logout():

    return redirect('http://127.0.0.1:5000/')


# @app.route('/user/<int:id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)


if __name__ == '__main__':
    app.run()
