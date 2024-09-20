from pydantic import BaseModel, Field, PositiveInt, StrictStr
from typing import Annotated, List
from datetime import date

class CharacterBase(BaseModel):
    name: Annotated[str, Field(..., min_length=1, description="Character's name")]
    eye_color: Annotated[str, Field(..., min_length=1, description="Character's eye color")]
    height: Annotated[PositiveInt, Field(..., description="Character's height, must be greater than 0")]
    mass: Annotated[PositiveInt, Field(..., description="Character's mass, must be greater than 0")]
    birth_year: Annotated[PositiveInt, Field(..., le=date.today().year, description="Character's year of birth, must be a valid year")]

class CharacterExtended(CharacterBase):
    hair_color: Annotated[str, Field(..., min_length=1, description="Character's hair color")]
    skin_color: Annotated[str, Field(..., min_length=1, description="Character's skin color")]

    class Config:
        extra = 'forbid'
        
class CharacterList(CharacterBase):
    id: int = Field(..., description="Unique identifier for the character")

class CharacterDetail(CharacterExtended):
    id: int = Field(..., description="Unique identifier for the character")



