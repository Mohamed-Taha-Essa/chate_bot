# Main application routes (home, profile)
from flask import Blueprint, render_template, request
from flask_socketio import emit, join_room
from flask_login import login_required, current_user
from .extention import socketio
from .models import User ,create_conversation , create_message , get_conversation , get_messages


chat = Blueprint('chat', __name__)

@chat.route('/')
def chathome():
    users = User.query.all()
    return render_template("chat.html", users=users)



@login_required
@chat.route('/chat_with/<int:user_id>')
def chat_with(user_id):
    other_user = User.query.get_or_404(user_id)

    #are thter any conversation between us 
    conv = get_conversation(current_user.id , user_id)
    if not conv:
        conv = create_conversation(current_user.id , user_id)

    messages = get_messages(conv.id)

    return render_template("chat.html", other_user=other_user ,  conversation=conv , messages=messages ,users=User.query.all() )


@socketio.on('join_conversation')
def join_conversation(conversation_id):
    join_room(str(conversation_id))

@socketio.on('message')
def handle_message(data):
    text = data['text']
    conversation_id = data['conversation_id']
    
    msg = create_message(conversation_id, current_user.id, text)
    
    emit(
        "message",
        {"id": msg.id, "content": text, "sender_id": current_user.id},
        room=str(conversation_id)
    )
