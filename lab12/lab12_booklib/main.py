import os
import nest_asyncio
import databases
import sqlalchemy
import ormar
from fastapi import FastAPI, HTTPException
from ormar.exceptions import NoMatch

# Застосовуємо nest_asyncio для стабільної асинхронної роботи
nest_asyncio.apply()

# Зчитатування змінної середовища для підключення до БД
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://user:password@localhost:5432/booksdb"
)

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()
engine = sqlalchemy.create_engine(DATABASE_URL)

app = FastAPI(title="Books API")


# Створення моделі даних Ormar без зовнішніх ключів
class Book(ormar.Model):
    class Meta:
        tablename = "books"
        metadata = metadata
        database = database

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=100)
    description: str = ormar.Text()
    published_year: int = ormar.Integer()


# Функція додавання початкових даних (seed)
async def seed_data():
    if await Book.objects.count() == 0:
        books_data = [
            {
                "title": "1984",
                "description": "Dystopian novel",
                "published_year": 1949,
            },
            {
                "title": "To Kill a Mockingbird",
                "description": "Classic novel",
                "published_year": 1960,
            },
            {
                "title": "The Great Gatsby",
                "description": "Novel by F. Scott Fitzgerald",
                "published_year": 1925,
            },
        ]
        for b in books_data:
            await Book.objects.create(**b)
        print("Початкові дані успішно додані в базу!")


# Події життєвого циклу додатка (startup / shutdown)
@app.on_event("startup")
async def startup():
    metadata.create_all(engine)
    if not database.is_connected:
        await database.connect()
    await seed_data()


@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()


# API Ендпоїнти
@app.get("/books/", tags=["Books"])
async def get_all_books():
    return await Book.objects.all()


@app.get("/books/{book_id}", tags=["Books"])
async def get_book_by_id(book_id: int):
    try:
        book = await Book.objects.get(id=book_id)
        return book
    except NoMatch:
        raise HTTPException(status_code=404, detail="Книга не знайдена")