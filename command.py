import redis
from models.post import Post

post = Post()

class Command(object):
    def __init__(self):
        print "init command"
    def touch(self,title):
        f = open("texts/" + title + ".md","w")
        f.close()
        

    # insert file body into redis database
    def migrate(self,filename):
        f = open("texts/" + filename + ".md")
        print f.read()

