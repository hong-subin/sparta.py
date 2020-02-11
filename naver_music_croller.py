import requests
import bs4

def get_song_ranks(count):
    header = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
    }
    response = requests.get('https://music.naver.com/',headers=header)

    html = response.text

    soup = bs4.BeautifulSoup(html, 'html.parser')

    songs = soup.select('tr._tracklist_move._track_dsc')

    ranks = []
    for song in songs[:count]:
        title = song.select_one('td.name a')
        artist = song.select_one('td.artist a')
        ranking = song.select_one('td.ranking span')

        info = {
            'ranking': ranking.text,
            'title': title.text,
            'artist': artist.text
        }
        ranks.append(info)

    return(ranks)