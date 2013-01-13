from nose.tools import ok_,eq_
import redis
from models.post import Post
from lib.settings import Settings
r = Settings.r

post = Post()

def setup():
    print "start"
    r.flushdb()

def create_test():
    """ create post posts:<id>:body:<value>"""
    post.create("a")
    eq_(r.get("posts:1:body"),'a')
    ok_(r.get("posts:1:created_at"))


def update_test():
    post.update(1,{"body":"update"})
    eq_(r.get("posts:1:body"),"update")

def destroy_test():
    """ destroy post """
    post.destroy(1)
    eq_(r.get("posts:1"),None)


def all_test():
    """ return all posts"""
    post.all()



def test_finish():
    print "called finish"
def tear_down():
    r.flushdb()

