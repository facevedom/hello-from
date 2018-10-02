from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    local_ip = socket.gethostbyname(socket.gethostname())
    return "Hello from {}".format(local_ip)