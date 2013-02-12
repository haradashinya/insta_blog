# -*- coding:utf-8 -*-
from flask import Flask
import redis
import json
import markdown
from flask import render_template,session
from flask import request,url_for
from flask import flash,redirect
from models.post import Post
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
import code
import hashlib
from werkzeug.security import generate_password_hash,check_password_hash
app = Flask(__name__)
app.secret_key = "admin"


m = hashlib.md5()
r = redis.StrictRedis(host="localhost",port=6379,db=0)
#r.set("blog0219:password",generate_password_hash("harashin0219"))

pagination_info = {
        "from":0,
        "to":5
        }

#### helper methods

def previous_page():
    post = Post()
    if  pagination_info["to"] < post.count():
        pagination_info["from"] += 5
        pagination_info["to"] += 5


def next_page():
    post = Post()
    print pagination_info
    if pagination_info["from"]  > 0:
        pagination_info["from"] -= 5
        pagination_info["to"] -= 5


def render_posts(admin):
    post = Post()
    return render_template("posts.html" ,
            posts = post.all(pagination_info["from"],pagination_info["to"]),p = post,admin= False)




@app.route("/")
def index():
    # show all blog page
    return render_template("index.html")

@app.route("/login",methods = ["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        if request.form["username"] != r.get("blog0219:username"):
            error = "Invalid Username"
        elif not check_password_hash(r.get("blog0219:password"),request.form["password"]):
            error = "Invalid Password"
        else:
            session["logged_in"] = True
            flash("You were logged in")
            return redirect("/posts")
        return render_template("login.html",error = error)


@app.route("/logout")
def logout():
    post = Post()
    session.pop("logged_in",None)
    flash("You were logged out")
    return     render_posts(admin = False)



@app.route("/preview")
def preview_page():
    return render_posts(False)


def md_compile(text):
    return json.dumps({"text":markdown.markdown(u"%s" % text)})




@app.route("/posts/<post_id>",methods=["GET"])
def show_post(post_id):
    _body = r.get("posts:%s:body" % post_id)
    return  render_template("show_post.html",body = markdown.markdown(_body.decode("utf-8"),))


@app.route("/posts",methods=["GET","POST"])
def post():
    post = Post()
    if request.method == "POST":
        text =  request.form["text"]
        if text != "":
            post.create(u"%s" % text)
            flash("created")
            return redirect("/posts")
    elif request.method == "GET":
        if session:
            admin = True
        else:
            admin = False
        return render_posts(admin)

    elif request.method == "DELETE":
        flash("destroyed")
        return render_posts()


@app.route("/delete_post/<post_id>",methods=["POST"])
def delete_post(post_id):
    post = Post()
    post.destroy(post_id)
    flash("destroy")
    return redirect("/posts")

@app.route("/update_post/<post_id>",methods=["POST"])
def update_post(post_id):
    text =  request.form["text"]
    r.set("posts:%s:body" % post_id,text)
    flash("updated")
    return redirect("/posts")



@app.route("/new_post",methods=["GET"])
def render():
    return render_template("new_post.html")


@app.route("/prev")
def prev():
    previous_page()
    return render_posts(False)

@app.route("/next")
def next():
    next_page()
    print ("callffl lnex")
    return render_posts(False)

# update text
@app.route("/edit_post/<post_id>")
def edit_post(post_id):
    _text =  r.get("posts:%s:body" % post_id).decode("utf-8")
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
