import redis
from datetime import datetime
r = redis.StrictRedis(host="localhost",port=6379,db=0)

class Article(object):
    def __init__(self):
        r.flushall()
        print("init")

    def time(self):
        return datetime.now().strftime("%Y %m/%d %H:%m")

    def create(self,text):
        id = r.incr("article_id")
        ns = "articles:%s" % id
        print(ns)
        r.hmset(ns,{"body":text,"created_at":self.time()})


    def update(self,id):
        pass

    def destroy(self,id):
        pass





