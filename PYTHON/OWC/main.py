from flask import Flask, render_template
from flask_socketio import SocketIo, send

app = Flask(__name__)
app.config["SECRET"] = "secret!123"
socketio = SocketIo(app, cors_allowed_origin="*")
