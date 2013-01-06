# -*- coding:utf-8 -*-
from flask import Flask
import redis
import json
import markdown
from flask import render_template
from flask import request,url_for
#from models.article import Article
from models.post import Post
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import code
app = Flask(__name__)


r = redis.StrictRedis(host="localhost",port=6379,db=0)
# create a instance of article
post = Post()

@app.route("/")
def index():
    # show all blog page
    return render_template("index.html")
@app.route("/foo/<id>")
def foo():
    print "hello"

def md_compile(text):
    return json.dumps({"text":markdown.markdown(u"%s" % text)})




@app.route("/posts/<post_id>",methods=["GET"])
def show_post(post_id):
    _body = r.get("posts:%s:body" % post_id)
    compiled_body = markdown.markdown(u"%s" % _body.decode("utf-8"))

    return  render_template("show_post.html",body = compiled_body )


@app.route("/posts",methods=["GET","POST"])
def post():
    post = Post()
    if request.method == "POST":
        text =  request.form["text"]
        post.create(u"%s" % text)
        id =  r.get("posts")
        return "success"
    elif request.method == "GET":
        return render_template("posts.html",posts = post.all(),p = post)
    elif request.method == "DELETE":
        return "removed"


@app.route("/delete_post/<post_id>",methods=["POST"])
def delete_post(post_id):
    post = Post()
    post.destroy(post_id)
    return "destroy"

@app.route("/update_post/<post_id>",methods=["POST"])
def update_post(post_id):
    text =  request.form["text"]
    r.set("posts:%s:body" % post_id,text)
    return post_id



@app.route("/new_post",methods=["GET"])
def render():
    return render_template("new_post.html")

# update text
@app.route("/edit_post/<post_id>")
def edit_post(post_id):
    _text =  r.get("posts:%s:body" % post_id)
    return render_template("edit_post.html",id=post_id,text = _text)

@app.route("/compile",methods=["POST"])
# compile plain text to markdown
def compile():
    if request.method == "POST":
        text = markdown.markdown(u"%s" % request.form["text"])
        return json.dumps({"text": text})

@app.route("/show_compile",methods=["POST"])
def show_compile():
    return json.dumps({"text": "foo bar"});


if __name__ == "__main__":
    app.run(debug=True)
