import redis


class Settings(object):
    pass
Settings.is_production = False

if Settings.is_production:
    Settings.r = redis.StrictRedis(host='localhost',port=6379,db=10)
else:
    print "for test"
    Settings.r = redis.StrictRedis(host='localhost',port=6379,db=0)



print "called"
