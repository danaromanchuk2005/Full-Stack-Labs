import ormar
from database import database, metadata

class Human(ormar.Model):
    class Meta(ormar.ModelMeta):
        tablename = "human"
        database = database
        metadata = metadata

    id: int = ormar.BigInteger(primary_key=True, nullable=False)
    name: str = ormar.String(max_length=50)
    surname: str = ormar.String(max_length=50)
    age: int = ormar.Integer(minimum=0)

class Dog(ormar.Model):
    class Meta(ormar.ModelMeta):
        tablename = "dog"
        database = database
        metadata = metadata

    id: int = ormar.BigInteger(primary_key=True)
    name: str = ormar.String(max_length=50)
    age: int = ormar.Integer(minimum=0)
    is_male: bool = ormar.Boolean()
    owner: Human | dict | None = ormar.ForeignKey(Human)