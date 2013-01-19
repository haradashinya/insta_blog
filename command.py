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
        body =  f.read()
        attr = {'body': body}
        post.update(v,attr)
        path = os.getcwd()
        os.remove(path + "/texts/test.md")









command = Command()







def help():
    print "called help"

def main():
    args =  sys.argv
    arg = args[1]
    # v: id
    v = int(args[2])
    print args
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
        f = open("texts/" + 'test' + ".md")
        command.update(v,attr)

    elif arg == "destroy":







if __name__ == "__main__":
    main()



