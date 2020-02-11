import flask
import pymongo

server = flask.Flask('내서버')
client = pymongo.MongoClient('localhost', 27017)

# 만약 '/'주소로 누군가 오면,
@server.route('/')
def home():
    # 'Hello Flask'를 출력하자
    return flask.render_template('index.html')

@server.route('/about')
def about():
    return flask.render_template('about.html')

@server.route('/users')
def users():
    users = [
        {'name': '수빈', 'gender': 'F'},
        {'name': '수빈', 'gender': 'F'},
        {'name': '수빈', 'gender': 'F'}
    ]
    return flask.jsonify(users)

@server.route('/movie')
def movie():
    movie = list(client.sparta.movie.find({}, {'_id': False}))
    return flask.jsonify(movie)


server.run(port=5000, debug=True)