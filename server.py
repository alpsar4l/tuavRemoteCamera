import flask
from flask import Flask
import serial
import time

from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
app.config["DEBUG"] = True
socketio = SocketIO(app)


@app.route("/")
def index():
    return flask.render_template("index.html")


@socketio.on("image")
def send_data(image):
    socketio.emit("show image", image.decode("UTF-8").strip())


socketio.run(app)
