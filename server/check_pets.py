from app import app, db
from models import Pet

with app.app_context():
    pets = Pet.query.all()
    print(pets)
