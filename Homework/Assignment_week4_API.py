from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/song_all', methods=['GET'])
def song_all():
    # 몽고 디비에서 검색
    all_songs = list(db.songs.find())
    result = dict()
    num = 0
    for song in all_songs:  # 반복문을 돌며 모든 결과값을 보기
        result[num] = {'rank' : song['rank'],'title':song['title'],'artist':song['artist']}
        num += 1
    return result


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)