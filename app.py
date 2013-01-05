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

@app.route("/edit_post")
def edit_post():
    return render_template("edit_post.html")




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
        print "called delete"
        return "removed"


@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    post = Post()
    post.destroy(post_id)
    return "destroy"




@app.route("/new_post",methods=["GET"])
def render():
    return render_template("new_post.html")


@app.route("/compile",methods=["POST"])
# compile plain text to markdown
def compile():
    if request.method == "POST":
        text = markdown.markdown(u"%s" % request.form["text"])
        return json.dumps({"text": text})





if __name__ == "__main__":
    app.run(debug=True)
