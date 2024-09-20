from fastapi import APIRouter, Depends, status, Response
from fastapi.responses import JSONResponse
from fastapi_pagination import Page, add_pagination
from sqlalchemy.orm import Session
from typing import List
from src.core.database import get_db
from src.use_cases.character.use_cases import fetch_characters, fetch_character, create_character, delete_character
from src.api.v1.schemas import CharacterList, CharacterDetail, CharacterExtended

router = APIRouter()

@router.get("/getAll", response_model=Page[CharacterList], status_code=status.HTTP_200_OK)
async def get_all(db: Session = Depends(get_db)):
    characters = fetch_characters(db)
    return characters

@router.get("/get/{id}", response_model=CharacterDetail, status_code=status.HTTP_200_OK)
async def get(id: int,  response: Response, db: Session = Depends(get_db)):
    character = fetch_character(id, db)
    if character is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, 
            content={"message": f"Character with id {id} doesn't exist"}
            )
    return character

@router.post("/add", response_model=CharacterDetail, status_code=status.HTTP_201_CREATED)
async def add(character: CharacterExtended, db: Session = Depends(get_db)):
    try:
        return create_character(character, db)
    except Exception as e:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            content={"message": str(e)}
            )

@router.delete("/delete/{id}", status_code=status.HTTP_200_OK)
async def delete(id: int, response: Response, db: Session = Depends(get_db)):
    character = delete_character(id, db)
    if character is None:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"message": f"Character with id {id} doesn't exist"}
    return {"message": f"character {character.id} ({character.name}) deleted successfully" } 
    