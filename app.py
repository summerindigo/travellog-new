from flask import Flask, render_template, jsonify , request
app = Flask(__name__)

## HTML 화면 보여주기
@app.route('/')        ## 우리의 여행일기 주소 : /
def home():            ## 우리의 여행일기 : home
    return render_template('index.html')

@app.route('/write')   ## 일기쓰기 주소 : write
def write():           ## 일기쓰기 : write
    return render_template('write.html')

@app.route('/mylog')   ## 내일기 모아보기 주소 : mylog
def mylog():           ## 내일기 모아보기 : mylog
    return render_template('mylog.html')


## API 역할을 하는 부분
@app.route('/log', methods=['POST'])
def write_log():
    test_receive = request.form['test_give']
    print(test_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


