#coding:utf-8

from flask import Flask
from flask import render_template
from Flask开发.models import Article # 导入模型
from flask import request
#创建一个应用实例
app = Flask(__name__)

#使用装饰器来完成路由
@app.route("/")
@app.route("/regiter",methods = ["POST","GET"])
#路由指定的视图函数
def index():
    articles = Article.select() # 查询数据库所有语句，类似于 select * from
    return render_template("index.html",articles = articles)
def regiter():
    if request.method == "POST":
        requestData = request.form  # 获取表单提交信息 得到是一个字典
        try:
            title = requestData["title"]
            author = requestData["author"]
            time = requestData["time"]
            description = requestData["description"]
            content = requestData["content"]

            # 实例化模型，保存数据
            article = Article()
            article.title = title
            article.author = author
            article.time = time
            article.description = description
            article.content = content
            article.save()
        except:
            return "404"

    return render_template("register.html")


if __name__ == "__main__":
    app.run() #启动实例