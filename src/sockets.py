# Main application routes (home, profile)
from flask import Blueprint, render_template, request
from flask_socketio import emit
from .extention import socketio
from .models import User


chat = Blueprint('chat', __name__)

@chat.route('/')
def chathome():
    users = User.query.all()
    return render_template("chat.html", users=users)


@socketio.on('message')
def handle_message(message):
    print('message: ', message)
    emit('message', {'text': message, 'sender': request.sid} ,broadcast=True)

