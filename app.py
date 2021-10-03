from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@15.164.50.230:27017')
db = client.travellog_project

from datetime import datetime   ## file 저장 명칭을 위해 필요

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


## 포스트 작성 페이지 write.html
@app.route('/write', methods=['POST'])
def write_log():            ## 일기 저장 버튼 누르면
    id_writer_receive = request.form['writer_give']
    id_numbers_receive = request.form['numbers_give']
    place_receive = request.form['place_give']
    title_receive = request.form['title_give']
    # date - 아래에 mydate
    weather_receive = request.form['weather_give']
    # file - 아래에 작성
    comment_receive = request.form['comment_give']
    print(request.data)

    # file = request.files['file_give']
    # extension = file.filename.split('.')[-1]  ## 확장자 이름 jpg png pdf 등

    today = datetime.now()
    mytime = today.strftime('%Y%m%d-%H%M%S') ## 예시 20200901-125956 -> 2020년 9월 1일 12시 59분 56초 인것
    mydate = today.strftime('%Y-%m-%d') ## 달력에서 날짜 선택하면 2020-10-10 형식으로 나오도록


    # filename = f'file-{mytime}'
    # save_to = f'static/{filename}.{extension}' ## static파일에 사진이 저장됨
    # file.save(save_to)

    doc = {
        'writer': id_writer_receive,
        'numbers': id_numbers_receive,
        'place': place_receive,
        'title': title_receive,
        'date': mydate,
        'weather': weather_receive,
        # 'file': f'{filename}.{extension}',
        'comment': comment_receive
    }

    db.travelLog.insert_one(doc)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)