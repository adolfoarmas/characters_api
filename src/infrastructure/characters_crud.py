from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from src.domain.character.models import Character
from src.api.v1.schemas import CharacterBase

def get_characters(db: Session):    
    return paginate(db, select(Character))   

def get_character(id: int, db: Session):
    return db.query(Character).filter(Character.id == id).first()
    

def add_character(character: CharacterBase, db: Session):
    db_character = Character(**character.model_dump())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

def delete_character(id, db: Session):
    db_character = db.query(Character).filter(Character.id == id).first()
    if db_character:
        db.delete(db_character)
        db.commit()
        return db_character
    return None

