#!flask/bin/python
import json
from flask import Flask, request, render_template, Response
from helloworld import playlist, songs
from helloworld.flaskrun import flaskrun
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

app.register_blueprint(playlist.bp)
app.register_blueprint(songs.bp)  

@app.route('/get-song', methods=['POST'])
def get_song():
    search_term = request.form['song_name']
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@app.route('/form')
def renderform():
    return render_template('form.html')            

if __name__ == '__main__':
    flaskrun(app)
