import redis 
import sys
import os
from models.post import Post
from optparse import OptionParser

post = Post()

class Command(object):
    def __init__(self):
        pass
    def touch(self,title,id):
        if id:
            body = post.find(int(id))
            f = open("texts/" + title + ".markdown","w")
            f.write("#" + body)
        else:
            f = open("texts/" + title + ".markdown","w")
            f.write("#")
        
        f.close()

    # insert file body into redis database
    def migrate(self,filename):
        f = open("texts/" + filename + ".markdown")
        body =  f.read()
        post.create(body)
        path = os.getcwd()
        os.remove(path + "/texts/test.markdown")





    def destroy(self,id):
        post.destroy(id)

    def show_all(self):
        return post.all()


    """ attr is like this ... """
    """ attr {"body" : "your post content"}"""
    def update(self,id,attr):
        if self.confirm_update(id,attr) == True:
            post.update(id,attr)
            path = os.getcwd()
            os.remove(path + "/texts/test.markdown")
            print "\nupdated!"
        else:
            print "quitted"

    def confirm_update(self,id,attr):
        print "you update this article. are you ok? if ok , press yes"
        print post.find(id)
        print "\n to\n"
        print attr['body']
        raw = raw_input("Enter yes or no,please  \n ")
        if raw == "yes":
            return True
        else:
            return False
        
    def confirm_destroy(self,id):
        print "you destroyed this article, are you ok?"
        print post.find(id) 
        print "\n"
        raw = raw_input("Enter yes or no , please")
        if raw == "yes":
            return True
        else:
            return False


command = Command()







def help():
    print "called help"

def main():
    args =  sys.argv
    arg = args[1]
    v = None
    if len(args) >= 3:
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
        if v != None:
            command.touch("test",v)
        else:
            command.touch("test",None)
        print """create text/test.markdown! feel free to
        edit"""
    elif arg == "migrate":
        command.migrate("test")
        print "called migrate"
    elif arg == "update":
        ff = open("texts/" + 'test' + ".markdown")
        body = ff.read()
        ff.close()
        command.update(int(v),{"body": body})

    elif arg == "destroy":
        if command.confirm_destroy(int(v)) == True:
            command.destroy(int(v))
            print "destroyed"
        else:
            print "cancel destroyed"


    elif arg == "all":
        for body in  command.show_all():
            print body['id'] + "\n"
            print body['body']








if __name__ == "__main__":
    main()



