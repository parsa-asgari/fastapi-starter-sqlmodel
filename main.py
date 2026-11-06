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
