from flask import Flask, render_template

app = Flask(__name__)


## HTML 화면 보여주기
@app.route('/')        ## 우리의 여행일기 주소 : /
def home():          ## 우리의 여행일기 : home
    return render_template('index.html')

@app.route('/write')   ## 일기쓰기 주소 : write
def write():           ## 일기쓰기 : write
    return render_template('write.html')

@app.route('/mylog')   ## 내일기 모아보기 주소 : mylog
def mylog():           ## 내일기 모아보기 : mylog
    return render_template('mylog.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)



## 변수명 변경 (주소 + 함수명 : memu1, record -> write / travle -> home)