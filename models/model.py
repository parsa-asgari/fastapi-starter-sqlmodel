# SQLModel-ORM imports
from sqlmodel import Field, SQLModel

class SampleModel(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    name: str
