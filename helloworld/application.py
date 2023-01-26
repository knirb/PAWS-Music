#!flask/bin/python
import json
from flask import Flask, Response, render_template
import playlist
from helloworld.flaskrun import flaskrun
import awscontroller

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello Worldddd'}), mimetype='application/json', status=200)

@app.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200) 

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/playlists/')
def playlists():
    return render_template('playlists.html')

app.register_blueprint(playlist.bp)

@app.route('/get-songs', methods=['GET'])
def get_songs():
    return awscontroller.get_songs()


if __name__ == '__main__':
    flaskrun(app)
