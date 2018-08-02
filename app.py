import string
from urllib.parse import quote

from flask import Flask, Response, jsonify, request, render_template

from entity import AppDetailResponse, UploadAppDetailResponse, Result
from flask_pymongo import PyMongo
import urllib3

from firsebase import cloud_push
from reptile import reptile

import firebase_admin
from firebase_admin import credentials


class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)


app = Flask(__name__)
app.response_class = MyResponse
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)

url = quote('https://gank.io/api/data/福利/10/', safe=string.printable)
urllib3.disable_warnings()


@app.route('/')
def hello_world():
    return render_template('monkey.html')


@app.route('/reptile')
def start_reptile():
    # http = urllib3.PoolManager()
    # res = http.request('GET', url + '1')
    # 开始爬
    reptile()
    return Result(True, '开始爬取...')


@app.route('/getAppDetail.do', methods=['GET'])
def get_detail():
    return AppDetailResponse("1", "1", "1", "1", "1", "1").__dict__


@app.route("/uploadAppDetail.do", methods=['POST'])
def upload_detail():
    print(request.form)
    return UploadAppDetailResponse("a", "b", "c", "d", "e").__dict__


@app.route('/postToken', methods=['POST'])
def receive_token():
    print(request.data)
    return ''


@app.route('/push')
def push():
    # 连接FCM进行推送
    return cloud_push()


if __name__ == '__main__':
    # Firebase
    cred = credentials.Certificate(r'firsebase\tiny_serviceAccountKey.json')
    firebase_admin.initialize_app(cred)
    # Flask
    app.debug = True
    app.run(host="0.0.0.0", port=80)
