import redis


class Settings(object):
    pass
Settings.is_production = False








if Settings.is_production:
    print "*************production-mode**********"
    Settings.r = redis.StrictRedis(host='localhost',port=6379,db=10)
else:
    print "*************debug-mode**********"
    Settings.r = redis.StrictRedis(host='localhost',port=6379,db=0)



print "called"
