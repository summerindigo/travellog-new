from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbtravelLog

## HTML 화면 보여주기
@app.route('/')
def travel():
    return render_template('index.html')

@app.route('/menu1')
def record():
    return render_template('write.html')

## API 역할을 하는 부분
@app.route('/log', methods=['POST'])
def make_Log():
    writer_receive = request.form['writer_give']
    code_receive = request.form['code_give']
    place_receive = request.form['place_give']
    title_receive = request.form['title_give']
    date_receive = request.form['date_give']
    weather_receive = request.form['weather_give']
    picture_receive = request.form['picture_give']
    memo_receive = request.form['memo_give']

    doc = {
        'writer': writer_receive,
        'code': code_receive,
        'place': place_receive,
        'title': title_receive,
        'date': date_receive,
        'weather': weather_receive,
        'picture': picture_receive,
        'memo': memo_receive
           }
    db.travelLog.insert_one(doc)

    return jsonify({'msg': '저장 완료!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
