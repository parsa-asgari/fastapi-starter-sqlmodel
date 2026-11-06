# FastAPI imports
from fastapi import FastAPI, Depends
from models.model import Person
from sqlmodel import Field, Session, SQLModel, create_engine, select
from utils.db import get_session, engine
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables if they don't exist
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/post_data")
def post_data(person: Person, session: Session = Depends(get_session)):
    with Session(engine) as session:
        session.add(person)
        session.commit()
        session.refresh(person)
        session.close()
        return person

    return { "status": "Successfully created new user." }