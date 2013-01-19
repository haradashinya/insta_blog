import redis
import sys
import os
from models.post import Post
from optparse import OptionParser

post = Post()



class Command(object):
    def __init__(self):
        pass
    def touch(self,title):
        f = open("texts/" + title + ".md","w")
        f.write("#")
        f.close()
        

    # insert file body into redis database
    def migrate(self,filename):
        f = open("texts/" + filename + ".md")
        body =  f.read()
        post.create(body)
        path = os.getcwd()
        os.remove(path + "/texts/test.md")

    def destroy(self,id):
        post.destroy(id)

    def show_all(self):
        return post.all()


    """ attr is like this ... """
    """ attr {"body" : "your post content"}"""
    def update(self,id,attr):
        post.update(id,attr)
        path = os.getcwd()
        os.remove(path + "/texts/test.md")


command = Command()







def help():
    print "called help"

def main():
    args =  sys.argv
    arg = args[1]
    v = args[2]
    # v: id
    if arg == "--v":
        print "1.0"
        return True
    elif arg == "--h":
        print """
            touch  create text file
            migrate migrate text file
        """
    elif arg == "touch":
        print "called touch"
        command.touch("test")
        print """create text/test.md! feel free to
        edit"""
    elif arg == "migrate":
        command.migrate("test")
        print "called migrate"
    elif arg == "update":
        ff = open("texts/" + 'test' + ".md")
        body = ff.read()
        print body.decode('utf-8')
        ff.close()
        command.update(int(v),{"body": body})

    elif arg == "destroy":
        command.destroy(int(v))







if __name__ == "__main__":
    main()



