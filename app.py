from flask import Flask
from flask import render_template
from flask import request,url_for
from models.article import Article
app = Flask(__name__)


# create a instance of article
article = Article()

@app.route("/")
def index():
    # show all blog page
    return render_template("index.html")



@app.route("/posts",methods=["GET","POST"])
def post():
    if request.method == "POST":
        return "success"
    elif request.method == "GET":
        # render create post page.
        return render_template("new_post.html")






if __name__ == "__main__":
    app.run(debug=True)
