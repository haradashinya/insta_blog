# -*- coding: utf-8 -*-
import redis
import json
from datetime import datetime
r = redis.StrictRedis(host="localhost",port=6379,db=0)

class Article(object):
    def __init__(self):
        """ remove all texts"""
        r.flushall()

    def time(self):
        return datetime.now().strftime("%Y %m/%d %H:%m")

    def create(self,text):
        id = r.incr("article_id")
        json_data = {"id": id,"body":text + " " + str(id),"created_at":self.time()}
        encoded_data = json.dumps(json_data,indent=4)
        r.lpush("texts",encoded_data)
        # data is json
        for data in r.lrange("texts",0,10):
            dict_data = json.loads(encoded_data)
        # json.loads is equal to JSON.parse




    def all(self):
        data_len =  r.llen("texts")
        return [json.loads(data) for data in r.lrange("texts",0,data_len)]

    def update(self,id,attr):
        target =  r.lindex("texts",id)
        """ update body str"""
        data  = json.loads(target)
        #data =  json.loads(json.dumps(target))
        data["body"] = attr["body"].encode('utf-8')
        r.lset("texts",id,json.dumps(data))

    def destroy(self,id):
        target = self.find(id)
        data_len = r.llen("texts")
        idx = 0
        for i in range(0,data_len):
            idx += 1
            if data_len - idx == id:
                item =  r.lindex('texts',idx)
                # remove item element from 'texts'
                r.lrem("texts",-1,item)
        items =  [json.loads(data) for data in r.lrange("texts",0,10)]
        print "id is"
        for i in items:
            print i["id"]

    #return output data as a dict 
    def find(self,id,is_json=False):
        data_len =  r.llen("texts") 
        res = [json.loads(data) for data in r.lrange("texts",0,data_len) if json.loads(data)["id"] == id]
        if len(res) > 0:
            return res[0]
        else:
            return False





