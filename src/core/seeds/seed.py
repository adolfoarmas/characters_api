from sqlalchemy.orm import Session
from src.core.database import SessionLocal
from src.domain.character.models import Character  # Replace with your actual models
from src.core.seeds.mock_characters import characters

def seed_data(db: Session):
    if not db.query(Character).first():
        for character in characters:
            character_db = Character(**character)
            db.add(character_db)
            db.commit()

def seed_database():
    db = SessionLocal()
    try:
        seed_data(db)
    finally:
        db.close()