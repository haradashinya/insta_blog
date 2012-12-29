import redis
from datetime import datetime
r = redis.StrictRedis(host="localhost",port=6379,db=0)

class Article(object):
    def __init__(self):
        print("init")

    def time(self):
        return datetime.now().strftime("%Y %m/%d %H:%m")

    def create(self):
        print("called create")
        pass




