from flask import Flask
from .extention import db, login_manager, socketio,migrate

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions with app
    db.init_app(app)
    socketio.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    # Configure Flask-Login
    login_manager.login_view = 'auth.login'
  
    
    # User loader function for Flask-Login
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register blueprints
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Load socket events
    from . import sockets
    
    return app