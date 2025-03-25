from app import db, app
from models import Pet

def seed_data():
    # Sample data to seed the pets table
    pets = [
        Pet(name='Buddy', species='Dog'),
        Pet(name='Mittens', species='Cat'),
        Pet(name='Goldie', species='Fish')
    ]
    
    # Add and commit the sample data to the database
    db.session.add_all(pets)
    db.session.commit()
    print("Database seeded!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        seed_data()
