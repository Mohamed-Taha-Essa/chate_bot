# 🤖 ChatBot - Real-Time Messaging System

A professional, real-time chat application built with **Flask**, **SocketIO**, and **Alpine.js**. This system features secure authentication, private conversations, and a responsive UI.

---

## 🚀 Features

- **Real-Time Communication**: Instant messaging powered by WebSockets (Flask-SocketIO).
- **Secure Authentication**: User registration and login with hashed passwords (Flask-Login & Werkzeug).
- **Private Conversations**: Automated room creation for 1-on-1 chats.
- **Persistent Storage**: Full chat history saved in an SQLite database (SQLAlchemy).
- **Responsive Design**: Modern UI built with Bulma and Bootstrap, optimized for all devices.
- **Reactive Frontend**: Lightweight client-side logic using Alpine.js.
- **Database Migrations**: Managed schema updates with Flask-Migrate.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend** | Python / Flask |
| **Real-Time** | Flask-SocketIO (WebSockets) |
| **Database** | SQLite / SQLAlchemy |
| **Migrations** | Flask-Migrate (Alembic) |
| **Auth** | Flask-Login |
| **Frontend** | Alpine.js / Jinja2 |
| **Styling** | Bulma / Bootstrap 5 |

---

## 🏗️ Architecture Analysis

### 1. Backend Architecture
The application follows the **App Factory Pattern**, ensuring modularity and scalability. Routes are organized into **Blueprints**:
- `auth`: Handles user lifecycle (Sign up, Login, Logout).
- `main`: Manages static pages and user profiles.
- `chat`: Handles the messaging interface and SocketIO event orchestration.

### 2. Real-Time Flow
The system utilizes **SocketIO Rooms** to isolate conversations.
1. When a user opens a chat, they emit a `join_conversation` event.
2. The server adds the user's socket to a room identified by the `conversation_id`.
3. Messages sent to that room are broadcasted only to the participants, ensuring privacy and efficiency.

### 3. Data Model
- **User**: Stores identity and credentials.
- **Conversation**: A join table linking two users in a unique chat session.
- **Message**: Stores content, timestamps, and foreign keys to the sender and conversation.

### 4. Frontend Reactivity
**Alpine.js** is used to bridge the gap between static Jinja2 templates and real-time updates. It manages:
- WebSocket connection lifecycle.
- Appending new messages to the DOM without refresh.
- Automatic scrolling to the latest message.

---

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd chate_bot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install flask flask-sqlalchemy flask-login flask-socketio flask-migrate eventlet
   ```

4. **Initialize the database**:
   ```bash
   flask db upgrade
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

---

## 📝 Usage

- Access the app at `http://127.0.0.1:5000`.
- Register a new account or login.
- Select a user from the sidebar to start a real-time conversation.
- Enjoy seamless, instant messaging!

---

*Developed with ❤️ using Flask and Alpine.js*
