#!flask/bin/python
import json
from flask import Flask, Response, request, render_template
import playlist
import songs
from helloworld.flaskrun import flaskrun
import awscontroller
import spotifycontroller

app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def get():
#     return Response(json.dumps({'Output': 'Hello Worldddd'}), mimetype='application/json', status=200)

# @app.route('/', methods=['POST'])
# def post():
#     return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200) 

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/playlists/')
def playlists():
    return render_template('playlists.html')

app.register_blueprint(playlist.bp)
app.register_blueprint(songs.bp)

@app.route('/get-songs', methods=['GET'])
def get_songs():
    return awscontroller.get_songs()

@app.route('/get-playlists', methods=['GET'])
def get_playlists():
    return spotifycontroller.get_playlists()    

@app.route('/get-song', methods=['POST'])
def get_song():
    search_term = request.form['song_name']

    return spotifycontroller.get_song(search_term)

@app.route('/form')
def renderform():
    return render_template('form.html')            

if __name__ == '__main__':
    flaskrun(app)
