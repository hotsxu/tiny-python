from flask import Flask, Response, jsonify

from entity import AppDetailResponse


class MyResponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, (list, dict)):
            response = jsonify(response)
        return super(Response, cls).force_type(response, environ)


app = Flask(__name__)
app.response_class = MyResponse


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getAppDetail.do', methods=["GET"])
def get_detail():
    return AppDetailResponse("1", "1", "1", "1", "1", "1").__dict__


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
