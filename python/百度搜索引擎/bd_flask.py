# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 14:02
# @Author  : Amy
# @File    : bd_flask.py

from flask import Flask
from flask import render_template, request
from bd_spider import bdSpider

# Flask(import_name)
# print(__name__)
# __name__当前文件运行 --> __main__
# 其它脚本调用该脚本运行__name__-->import_name

app = Flask(__name__)


# 404-->服务器未找到该页面-->没有路由与视图
# @->装饰器,在不改变源代码的情况下为函数添加新的功能
@app.route("/hello")
def hello():
    return "hello world"


#  http://127.0.0.1:5000/amy-->hello everyone
@app.route("/amy")
def amy():
    return "hello everyone"


@app.route("/")
def index():
    # 1.代码不简洁2.不易维护
    # return '<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off"><input type="submit" value="百度一下" id="su" class="btn self-btn bg s_btn">'
    return render_template("index.html")


@app.route("/s")
def search():
    # 获取url参数
    kw = request.args.get('wd')
    html = bdSpider(kw)
    return html


app.run(debug=True)

