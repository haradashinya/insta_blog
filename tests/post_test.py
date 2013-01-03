from nose.tools import ok_,eq_
import redis
r = redis.StrictRedis(host="localhost",port=6379,db=0)
from models.post import Post

post = Post()

def setup():
    post

def create_test():
    """ create post posts:<id>:body:<value>"""
    post.create(u"apple")
    post.create(u"orange")
    eq_(r.get("posts:1:body"),"apple")
    eq_(r.get("posts:2:body"),"orange")
    eq_(r.get("posts:1:created_at"),post.time())

def update_test():
    post.update(1,{"body":"update"})
    eq_(r.get("posts:1:body"),"update")

def destroy_test():
    """ destroy post """
    post.destroy(1)
    eq_(r.get("posts:1"),None)




def test_finish():
    print "called finish"

