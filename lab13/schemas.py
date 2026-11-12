from pydantic import BaseModel, Field

class DogCreate(BaseModel):
    name: str = Field(max_length=50)
    age: int = Field(ge=0)
    is_male: bool
    owner: int | None = None

class DogUpdate(BaseModel):
    name: str | None = Field(None, max_length=50)
    age: int | None = Field(None, ge=0)
    is_male: bool | None = None
    owner: int | None = None

class HumanCreate(BaseModel):
    name: str = Field(max_length=50)
    surname: str = Field(max_length=50)
    age: int = Field(ge=0)

class HumanUpdate(BaseModel):
    name: str | None = Field(None, max_length=50)
    surname: str | None = Field(None, max_length=50)
    age: int | None = Field(None, ge=0)