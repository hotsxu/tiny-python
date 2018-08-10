import threading

from bson import ObjectId
from flask import Flask, Response, jsonify, request, render_template
import asyncio

from entity import Result
import pymongo

from firsebase import cloud_push
from reptile import reptile

import firebase_admin
from firebase_admin import credentials


# 处理service返回数据
class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)


app = Flask(__name__)
app.response_class = MyResponse
mongo_client = pymongo.MongoClient('mongodb://localhost:27017/')
db = mongo_client.tiny


# 处理ObjectId转str
def bson_process(bson):
    if isinstance(bson, dict):
        if bson['_id'] is not None:
            if isinstance(bson['_id'], ObjectId):
                bson['_id'] = str(bson['_id'])
    elif isinstance(bson, list):
        for obj in bson:
            if obj['_id'] is not None:
                if isinstance(obj['_id'], ObjectId):
                    obj['_id'] = str(obj['_id'])
    return bson


@app.route('/reptile')
def start_reptile():
    # 开始爬
    threading.Thread(target=reptile).start()
    return Result(True, '开始爬取...').__dict__


@app.route('/postToken', methods=['POST'])
def receive_token():
    print(request.data)
    return Result(True, "ok").__dict__


@app.route('/push')
def push():
    # 连接FCM进行推送
    return cloud_push()


@app.route('/get_cat')
def get_cat():
    cats = db.tiny.find()
    return Result(True, bson_process(list(cats))).__dict__


@app.route('/test')
def test():
    users = db.tiny.find({'name': 'ff'})
    # print(list(users))
    return Result(True, bson_process(list(users))).__dict__


if __name__ == '__main__':
    # Firebase
    cred = credentials.Certificate(r'firsebase\tiny_serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    # Flask
    app.debug = True
    app.run(host="0.0.0.0", port=80)
