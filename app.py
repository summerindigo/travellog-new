
from flask import Flask, render_template

app = Flask(__name__)


## HTML 화면 보여주기
@app.route('/')        ## home 페이지 - /
def travle():          ## 우리의 여행일기 - travle
    return render_template('index.html')

@app.route('/menu1')   ## 일기쓰기 페이지 - menu1
def record():          ## 일기쓰기 - record
    return render_template('write.html')

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

## 2021.09.29 완료 !