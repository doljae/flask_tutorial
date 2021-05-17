import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user', methods=['GET', 'POST'])
def userLogin():
    if request.method == "GET":
        url = ""
        res = requests.get(url=url)
        # print(res.status_code, type(res.text), res.url)
        return jsonify(res.text)
        pass
    elif request.method == "POST":
        # do something
        pass


# Spring의 @PathVariable 사용법
@app.route('/env/<language>')
def environments(language):
    return jsonify({"language": language})


if __name__ == '__main__':
    app.run(debug=True)
