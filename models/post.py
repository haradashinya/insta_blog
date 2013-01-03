import redis
from datetime import datetime
import json
import re
r = redis.StrictRedis(host="localhost",port=6379,db=0)
class Post(object):
    def __init__(self):
        print "init post"

    
    """ return all posts sort by order"""
    def all(self):
        res = r.keys("posts:*:created_at*")
        dates = []
        for i in res:
            id = i.split(":")[1]
            print id
            dates.append(
                    {"created_at":r.get(i),
                    "body":r.get("posts:%s:body" % id)
                    }
                    )
            dates.sort(key=lambda r: r["created_at"],reverse=True)
        return dates
        

    def latest(self):
        return r.get([res for res in r.keys("posts:%s*" % r.get("posts"))])


    def time(self):
        return datetime.now()


    def create(self,body):
        post_id =  r.incr("posts")
        #print post_id
        r.set("posts:%i:body" % (post_id),body)
        r.set("posts:%i:created_at" % (post_id),self.time())

    def update(self,id,attr):
        r.set("posts:%i:body" % id,attr['body']) 

    def destroy(self,id):
        for key in  r.keys("posts:%i*" % id):

            r.set("key",None)

    def body_to_created_time(self,body):
        for i in r.keys("*:created_at"):
            id =  i.split(":")[1]
            if body ==  r.get("posts:%s:body" % id):
                return r.get("posts:%s:created_at" % id)
        #is_body = re.compile('.*post')
        #is_date = re.compile('.*created_at')
        return "hello"

