import redis
import os
from models.post import Post

post = Post()



class Command(object):
    def __init__(self):
        pass
    def touch(self,title):
        f = open("texts/" + title + ".md","w")
        f.close()
        

    # insert file body into redis database
    def migrate(self,filename):
        f = open("texts/" + filename + ".md")
        body =  f.read()
        post.create(body)
        path = os.getcwd()
        os.remove(path + "/texts/test.md")
        print "body : %s migrate successfully" % body

    def destroy(self,id):
        post.destroy(id)

    def show_all(self):
        print post.all()
        return post.all()


    """ attr is like this ... """
    """ attr {"body" : "your post content"}"""
    def update(self,id,attr):
        post.update(1,{"body":"update"})



    def handle_command(self,cmd):
        pass



