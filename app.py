from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@15.164.50.230:27017')
db = client.travellog_project

from wordcloud import WordCloud
from PIL import Image
import numpy as np

from datetime import datetime   # file 저장 명칭을 위해 필요

# HTML 화면 보여주기
@app.route('/')        # 우리의 여행일기 주소 : /
def home():            # 우리의 여행일기 : home
    return render_template('index.html')

@app.route('/write')   # 일기쓰기 주소 : write
def write():           # 일기쓰기 : write
    return render_template('write.html')

# 내 일기 모아보기 변경-> 클라우드
@app.route('/cloud')   # 클라우드보기 주소 : cloud
def cloud():           # 클라우드 : cloud
    return render_template('cloud.html')

@app.route('/about')   # 웹사이트 크레딧 주소 : about
def about():           # 웹사이트 크레딧 : about
    return render_template('about.html')

# 포스트 작성 write.html
@app.route('/write', methods=['POST'])
def write_log():            # 일기 저장 버튼 누르면
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
    # extension = file.filename.split('.')[-1]   # 확장자 이름 jpg png pdf 등

    today = datetime.now()
    mytime = today.strftime('%Y%m%d-%H%M%S')     # 예시 20200901-125956 -> 2020년 9월 1일 12시 59분 56초 인것
    mydate = today.strftime('%Y-%m-%d')          # 달력에서 날짜 선택하면 2020-10-10 형식으로 나오도록


    # filename = f'file-{mytime}'
    # save_to = f'static/{filename}.{extension}' # static파일에 사진이 저장됨
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
    return jsonify({'result': 'success', 'msg': '오늘 일기 끝~!'})

# 포스트 보여주기 index.html
@app.route('/', methods=['POST'])
def show_logs():
    # 5. route 주소 변경
    travel_log = list(db.travelLog.find({}, {'_id': False}))
    return jsonify({'travel_logs' : travel_log})

# 워드클라우드 보여주기 cloud.html
@app.route('/cloud', methods=['GET'])
def show_cloud():
    wc.to_file("wordcloud.png")
    return jsonify({'word_clouds': '/making_proj/wordcloud.png'})

# 워드클라우드 만들기
# 1. 몽고디비에서 place, title, comment 가져오기
texts = list(db.travelLog.find({}, {'_id': False, 'writer': False, 'numbers': False, 'date': False, 'weather': False}))
for text in texts:
    place = text['place']
    title = text['title'].replace('!','').replace('~','').replace('.','')
    comment = text['comment'].replace('!','').replace('~','').replace('.','').replace(',','').replace('\n','')

    def cloud():
        return place + title + comment
    # print(cloud())

# 2. 워드클라우드 만들기
# 클라우드 모양 지정하기
mask = np.array(Image.open('cloud.png'))
# 워드클라우드 테마 바꾸기
palettes = ['Pastel1', 'Pastel2', 'Set1', 'Set2', 'Set3', 'Paired', 'Accent', 'Dark2']

wc = WordCloud(background_color='white',
               # 윈도우 폰트
               font_path='C:/Windows/Fonts/Hancom Gothic Regular.ttf',
               # 맥 폰트
               # font_path='C:/System/Library/Fonts/Supplemental/AppleGothic.ttf',
               mask=mask,
               colormap='Dark2')

wc.generate(cloud())
wc.to_file("wordcloud.png")


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)