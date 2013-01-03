from flask import Flask
import redis

from flask import render_template
from flask import request,url_for
#from models.article import Article
from models.post import Post
import code
app = Flask(__name__)


r = redis.StrictRedis(host="localhost",port=6379,db=0)
# create a instance of article
post = Post()

@app.route("/")
def index():
    # show all blog page
    return render_template("index.html")





@app.route("/posts",methods=["GET","POST"])
def post():
    post = Post()
    if request.method == "POST":
        text =  request.form["text"].encode("utf-8")
        post.create(text)
        id =  r.get("posts")
        print r.get(r.keys("posts:%s:body" % id))
        
        
        return "success"
    elif request.method == "GET":
        # render create post page.
        return render_template("new_post.html")

@app.route("/new_post",methods=["GET"])
def render():
    return render_template("new_post.html")






if __name__ == "__main__":
    app.run(debug=True)
