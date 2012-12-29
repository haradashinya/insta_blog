from models.article import Article
from nose.tools import ok_,eq_
import re

article = Article()
def setup():
    pass
def add(a,b):
    return a + b

def add_test():
    """ex1.add test"""
    eq_(add(1,2),3)


def time_test():
    time =  article.time()
    # 2012 ...
    ok_(re.match(r'\d\d\d\d \d\d',time))


def create_test():
    print article.create()
    pass
    

