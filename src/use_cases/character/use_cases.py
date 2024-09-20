from sqlalchemy.orm import Session
from src.infrastructure.characters_crud import get_characters, get_character, add_character, delete_character as delete

def fetch_characters(db: Session):
    return get_characters(db)

def fetch_character(id: int, db: Session):
    return get_character(id, db)

def create_character(character, db: Session):
    return add_character(character, db)

def delete_character(id:int, db: Session):
    return delete(id, db)