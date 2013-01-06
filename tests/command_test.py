#coding:utf-8

from nose.tools import ok_,eq_
from command import Command

command = Command()
def touch_test():
    command.touch("test")
    f = open("texts/test.md","w")
    f.write(u"""
    #hello world 
    hello world
    hello world
    い""".encode("utf-8"))
    f.close()


def migrate_test():
    command.migrate("test")
    f = open("texts/test.md","r")
    body = f.read()
    ok_(body)
    f.close()


