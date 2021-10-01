from flask import Flask, render_template

app = Flask(__name__)


## HTML 화면 보여주기
@app.route('/')        ## home 페이지주소 : /
def travle():          ## 우리의 여행일기 : travle
    return render_template('index.html')

@app.route('/write')   ## 일기쓰기 페이지주소 : /menu1 -> /write
def write():           ## 일기쓰기 : record -> write
    return render_template('write.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

## 2021.09.29 완료 !

## 변수명 변경 제안 (일기쓰기주소 + 함수명 : memu1, record -> write)