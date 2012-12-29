from models.article import Article
from nose.tools import ok_,eq_
import redis
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
    """ create article """
    text = "this is a test text"
    article.create(text)
    article.create(text)
    


def all_test():
    """return all articles."""
    all_articles = article.all()

    """ all_article's type is should dict """
    eq_(type(all_articles[0]),type({"nobi": "foo"}))
    print all_articles
    

def update_test():
    """update article"""
    """change body and created_at"""
    article.update(1)

def destroy_test():
    """ destroy article"""
    pass




