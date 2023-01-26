#!flask/bin/python
from flask import Flask, request, render_template
import playlist
import songs
from helloworld.flaskrun import flaskrun
import spotifycontroller
import os

print(os.getenv("SPOTIPY_CLIENT_ID"))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

app.register_blueprint(playlist.bp)
app.register_blueprint(songs.bp)  

@app.route('/get-song', methods=['POST'])
def get_song():
    search_term = request.form['song_name']
    return spotifycontroller.get_song(search_term)

@app.route('/form')
def renderform():
    return render_template('form.html')            

if __name__ == '__main__':
    flaskrun(app)
