
from flask import Flask, render_template, jsonify, request 

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
# client = MongoClient('mongodb://test:test@localhost', 27017) 이건 일부러 비활성화 시킴
db = client. travellog_project

from datetime import datetime   ## file 저장 명칭을 위해 필요

## HTML 화면 보여주기
@app.route('/')        ## home 페이지 - /
def travle():          ## 우리의 여행일기 - travle
    return render_template('index.html')

@app.route('/menu1')   ## 일기쓰기 페이지 - menu1
def record():          ## 일기쓰기 - record
    return render_template('write.html')



## 포스트 작성 페이지 write.html
@app.route('/menu1', methods=['POST'])
def post():            ## 일기 저장 버튼 누르면
    id_writer_receive = request.form['writer_give']
    id_numbers_receive = request.form['numbers_give']
    place_receive = request.form['place_give']
    title_receive = request.form['title_give']
    ## date - 아래에 mydate 관련
    weather_receive = request.form['weather_give']
    ## file - 아래에 작성함
    comment_receive = request.form['comment_give']

    file = request.files['file_give']
    extension = file.filename.split('.')[-1]  ## 확장자 이름 jpg png pdf 등

    today = datetime.now()
    mytime = today.strftime('%Y%m%d-%H%M%S') ## 예시 20200901-125956 -> 2020년 9월 1일 12시 59분 56초 인것
    mydate = today.strftime('%Y-%m-%d') ## 달력에서 날짜 선택하면 2020-10-10 형식으로 나오도록


    filename = f'file-{mytime}' ## 파일명을 mytime으로 해서 겹치는 파일의 확률을 엄청 줄임
    save_to = f'static/{filename}.{extension}' ## static파일에 사진이 저장됨
    file.save(save_to)

    doc = {
        'writer': id_writer_receive,
        'numbers': id_numbers_receive,
        'place': place_receive,
        'title': title_receive, 
        'date' : mydate, 
        'weather' : weather_receive,
        'file' : f'{filename}.{extension}',
        'comment' : comment_receive
    }

    db.practice.insert_one(doc)
    return jsonify({'msg': '저장이 완료되었습니다'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

## 2021.09.29 완료 !