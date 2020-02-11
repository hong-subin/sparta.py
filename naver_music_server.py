import flask
import naver_music_croller


app = flask.Flask('네이버 음악 순위 서버')

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/music', methods=['POST'])
def post_music():
    return "POST Music"

@app.route('/music', methods=['GET'])
def music():
    try:
        count = flask.request.args['count']
    except:
        count = 5
    data = naver_music_croller.get_song_ranks(int(count))
    return flask.jsonify(data)

app.run(port=5000, debug=True)





