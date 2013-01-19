#coding:utf-8

from nose.tools import ok_,eq_
from command import Command
from models.post import Post
from lib.settings import Settings
r = Settings.r

command = Command()
post = Post()

def setup():
    r.flushdb()
    print "setup called"


def touch_test():
    command.touch("test")
    f = open("texts/test.markdown","w")
    body = u"あ".encode("utf-8").strip()
    f.write(body)
    f.close()

def command_test():
    """ handle command """
    f = open("texts/test.markdown",'r')
    print f.read()
    f.close()



def migrate_test():
    """ test.markdownのファイルを書き換える"""
    """ migrate(filename) """

    command.migrate("test")
    #f = open("texts/test.markdown","r")
    #body = f.read()
    #eq_(body.decode("utf-8"),u"あ")
    #eq_(r.get("posts:1:body").decode("utf-8"),u"あ")
    #f.close()

def show_all_test():
    """ return all post"""
    command.show_all()


def update_test():
    """ should update """
    command.update(1,{"body":"hello world"})
def destroy_test():
    """ should destroy post """
    """ destroy(<int id>)"""
    command.destroy(1)
    eq_(len(command.show_all()),0)

def handle_command_test():
    pass

def teardown():
    r.flushdb()



