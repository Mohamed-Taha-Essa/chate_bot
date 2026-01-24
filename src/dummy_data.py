from faker import Faker
from werkzeug.security import generate_password_hash

def create_dummy_users(count=10):
    """Create dummy users using Faker library."""
    import sys
    import os
    
    # Add the project root to Python path
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(project_root)
    
    from src.extention import db
    from src.models import User
    from src import create_app
    
    app = create_app()
    with app.app_context():
        fake = Faker()
        
        users = []
        for _ in range(count):
            user = User(
                name=fake.name(),
                email=fake.email(),
                password=generate_password_hash('password123')  # Default password for all dummy users
            )
            users.append(user)
            db.session.add(user)
        
        db.session.commit()
        print(f"Created {count} dummy users successfully!")
        
        return users

if __name__ == '__main__':
    create_dummy_users()