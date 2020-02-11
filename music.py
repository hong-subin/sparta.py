import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.


# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

ranks = soup.select('table.list-wrap tr.list')
for rank in ranks:
    title = rank.select_one('td.info a.title.ellipsis')
    ranking = rank.select_one('td.number')

    if title is not None:
        music = {'ranking': ranking.text.rstrip(),
                 'title': title.text.strip(),
                 'artist': rank.select_one('td.info a.artist.ellipsis').text
                 }
        #client.sparta.music.insert_one(music)
        print(music)

all_music = list(client.sparta.music.find({'_id':0}))
for music in all_music:
    print(music)


