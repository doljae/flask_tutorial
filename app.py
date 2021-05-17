import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/user', methods=['GET', 'POST'])
def userLogin():
    if request.method == "GET":
        url = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?serviceKey=5FhraaRadfDLuBUCpxvn0EPHOvG0I4PLHXb13X4vsrgAVMCXEQdmhbEqQney9x234XWKDeis4AdD6seUIVuInw%3D%3D&Q0=%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C&Q1=%EA%B0%95%EB%82%A8%EA%B5%AC&QT=1&QN=%EC%82%BC%EC%84%B1%EC%95%BD%EA%B5%AD&ORD=NAME&pageNo=1&numOfRows=10"
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
