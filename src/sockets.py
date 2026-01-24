# Main application routes (home, profile)
from flask import Flask, render_template, request
from flask_socketio import SocketIO ,emit



app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")


@socketio.on('message')
def handle_message(message):
    print('message: ', message)
    emit('message', {'text': message, 'sender': request.sid} ,broadcast=True)

