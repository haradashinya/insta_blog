# -*- coding: utf-8 -*-
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
    text = 'こんにちは'
    article.create(text)
    article.create(text)
    article.create(text)
    


def all_test():
    """return all articles."""
    all_articles = article.all()

    """ all_article's type is should dict """
    eq_(type(all_articles[0]),type({"nobi": "foo"}))
    

def find_test():
    """ article.find(1)'s id is 1 """
    eq_(article.find(1)["id"],1)


def destroy_test():
    """ destroy article"""
    article.destroy(2)
    eq_(article.find(2),False)
    eq_(len(article.all()),2)

def update_test():
    pass
    #article.update(1,{"body":"updated"})





