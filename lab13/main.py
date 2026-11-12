import sqlite3
from fastapi import FastAPI, Response
from fastapi.exceptions import HTTPException
from ormar.exceptions import NoMatch
from database import database, engine, metadata
from models import Dog, Human
from schemas import DogCreate, DogUpdate, HumanCreate, HumanUpdate

app = FastAPI()
app.state.database = database

@app.on_event("startup")
async def startup():
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
    metadata.create_all(engine)

@app.on_event("shutdown")
async def shutdown():
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

# --- HUMAN CRUD ---

@app.get("/human/")
async def get_humans():
    return await Human.objects.all()

@app.post("/human/")
async def create_human(human: HumanCreate):
    try:
        return await Human(**human.dict()).save()
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/human/{id}")
async def get_human_by_id(id: int):
    try:
        return await Human.objects.get(id=id)
    except NoMatch:
        raise HTTPException(status_code=404, detail=f"Human with id {id} not found!")

@app.patch("/human/{id}")
async def update_human(id: int, human: HumanUpdate):
    try:
        db_human = await Human.objects.get(pk=id)
        await db_human.update(**human.dict(exclude_unset=True))
        return db_human
    except NoMatch:
        raise HTTPException(status_code=404, detail=f"Human with id {id} not found!")

@app.delete("/human/{id}")
async def delete_human(id: int):
    try:
        await Human.objects.delete(id=id)
        return Response(status_code=204)
    except NoMatch:
        raise HTTPException(status_code=404, detail=f"Human with id {id} not found!")
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=409, detail=str(e))

# --- DOG CRUD ---

@app.get("/dog/")
async def get_dogs():
    return await Dog.objects.all()

@app.post("/dog/")
async def create_dog(dog: DogCreate):
    try:
        return await Dog(**dog.dict()).save()
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/dog/{id}")
async def get_dog_by_id(id: int):
    try:
        return await Dog.objects.get(id=id)
    except NoMatch:
        raise HTTPException(status_code=404, detail=f"Dog with id {id} not found!")

@app.patch("/dog/{id}")
async def update_dog(id: int, dog: DogUpdate):
    try:
        db_dog = await Dog.objects.get(pk=id)
        await db_dog.update(**dog.dict(exclude_unset=True))
        return db_dog
    except NoMatch:
        raise HTTPException(status_code=404, detail=f"Dog with id {id} not found!")

@app.delete("/dog/{id}")
async def delete_dog(id: int):
    try:
        await Dog.objects.delete(id=id)
        return Response(status_code=204)
    except NoMatch:
        raise HTTPException(status_code=404, detail=f"Dog with id {id} not found!")
    except sqlite3.IntegrityError as e:
        raise HTTPException(status_code=409, detail=str(e))