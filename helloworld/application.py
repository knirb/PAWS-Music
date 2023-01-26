#!flask/bin/python
from flask import Flask, request, render_template
from helloworld import playlist, songs
from helloworld.flaskrun import flaskrun
import os

print(os.getenv("SPOTIPY_CLIENT_ID"))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

# app.register_blueprint(playlist.bp)
# app.register_blueprint(songs.bp)  

# @app.route('/get-song', methods=['POST'])
# def get_song():
#     search_term = request.form['song_name']
#     # return spotifycontroller.get_song(search_term)
#     return 'badbing badaboom'

@app.route('/form')
def renderform():
    return render_template('form.html')            

if __name__ == '__main__':
    flaskrun(app)
