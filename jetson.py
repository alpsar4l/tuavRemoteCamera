import time
import socketio
import cv2
import base64


camera = cv2.VideoCapture(0)
sio = socketio.Client()


@sio.event
def connect():
    print("bağlantı kuruldu")


@sio.event
def disconnect():
    print("bağlantı uçtu")
    camera.release()


sio.connect('http://127.0.0.1:5000')

while True:
    success, frame = camera.read()
    ret, frame = cv2.imencode(".jpg", frame)
    data = base64.b64encode(frame)

    sio.emit("image", data)
    print("kamera çalışıyor")

    #  time.sleep(1)