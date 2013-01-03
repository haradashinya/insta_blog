import redis
from datetime import datetime
import json
r = redis.StrictRedis(host="localhost",port=6379,db=0)
class Post(object):
    def __init__(self):
        print "init post"

    
    """ return all posts"""
    def all(self):
        return [r.get(res) for res in r.keys("posts:*:body")]
    


    def latest(self):
        return r.get([res for res in r.keys("posts:%s*" % r.get("posts"))])


    def time(self):
        return datetime.now().strftime("%Y %m/%d %H:%m")

    def create(self,body):
        post_id =  r.incr("posts")
        #print post_id
        r.set("posts:%i:body" % (post_id),body)
        r.set("posts:%i:created_at" % (post_id),self.time())
        print r.get("posts:%i:body" %(post_id))

    def update(self,id,attr):
        r.set("posts:%i:body" % id,attr['body']) 

    def destroy(self,id):
        for key in  r.keys("posts:%i*" % id):
            r.set("key",None)

