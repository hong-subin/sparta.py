import bs4
import requests
import pymongo

response = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200203')
soup = bs4.BeautifulSoup(response.text, 'html.parser')

client = pymongo.MongoClient('localhost', 27017)

ranks = soup.select('table.list_ranking tr')
for rank in ranks:
    title = rank.select_one('div.tit5 a')
    score = rank.select_one('td.point')
    if title is not None:
        movie = {'title': title.text,
                 'score': float(score.text),
                 'link': 'https://movie.naver.com'+title['href']}
        #client.sparta.movie.insert_one(movie)
        print(movie)
#db에서 모든 영화 정보 읽기 (find)
all_movie = list(client.sparta.movie.find({'_id':0}))
#전부 출력하기
for movie in all_movie:
    print(movie)




