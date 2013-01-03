import redis
import json
r = redis.StrictRedis(host="localhost",port=6379,db=0)
class Post(object):
    def __init__(self):
        print "init post"



    def create(self,body):
        post_id =  r.incr("posts")
        #print post_id
        r.set("posts:%i:body" % (post_id),body)
        print r.get("posts:%i:body" %(post_id))

    def update(self,id,attr):
        pass
        #r.set("posts:%i:body" % (id,body),attr['body']) 

