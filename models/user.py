import redis
from lib.settings import Settings
from werkzeug.security import generate_password_hash
r = Settings.r

class User(object):
    def __init__(self):
        pass
    def create(self,name,password):
        r.set("blog0219:username",username)
        r.set("blog0219:password",generate_password_hash("harashin0219"))
