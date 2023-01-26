#!flask/bin/python
import json
from flask import Flask, Response, render_template
import playlist
import songs
from helloworld.flaskrun import flaskrun
import awscontroller

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

app.register_blueprint(playlist.bp)
app.register_blueprint(songs.bp)

@app.route('/get-songs', methods=['GET'])
def get_songs():
    return awscontroller.get_songs()


if __name__ == '__main__':
    flaskrun(app)
