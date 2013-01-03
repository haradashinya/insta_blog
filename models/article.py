# -*- coding: utf-8 -*-
import redis
import json
from datetime import datetime
r = redis.StrictRedis(host="localhost",port=6379,db=0)

class Article(object):
    def __init__(self):
        """ remove all db"""
        #r.flushall()
        print("init")

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




    def find(self,id):
        data_len = r.llen("texts")
        all_data = [data for data in r.lrange("texts",0,data_len) if json.loads(data)["id"] == id ]

        return all_data







    def destroy(self,id):
        pass


    #return output data as a dict 
    def find(self,id,is_json=False):
        data_len =  r.llen("texts")
        return [json.loads(data) for data in r.lrange("texts",0,data_len) if json.loads(data)["id"] == id][0]





