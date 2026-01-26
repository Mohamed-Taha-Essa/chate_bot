from . import db
from flask_login import UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # store hashed passwords
    name = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user1 = db.relationship('User', foreign_keys=[user1_id])
    user2 = db.relationship('User', foreign_keys=[user2_id])
    messages = db.relationship('Message', backref='conversation', lazy='dynamic')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)



def create_conversation(user_one_id , user_second_id):
    conversation = Conversation(user1_id=user_one_id, user2_id=user_second_id)
    db.session.add(conversation)
    db.session.commit()
    return conversation

def create_message(conversation_id , sender_id , content):
    message = Message(conversation_id=conversation_id , sender_id=sender_id , content=content)
    db.session.add(message)
    db.session.commit()
    return message

def get_conversation(user_one_id , user_second_id):
    return Conversation.query.filter(((Conversation.user1_id == user_one_id) & (Conversation.user2_id == user_second_id)) | ((Conversation.user1_id == user_second_id) & (Conversation.user2_id == user_one_id))).first()
   

def get_messages(conversation_id):
    return Message.query.filter_by(conversation_id=conversation_id).all()

