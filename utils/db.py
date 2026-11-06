from sqlmodel import Session, create_engine

postgres_connection_string = "postgresql://postgres:postgres@localhost/mydb"
engine = create_engine(postgres_connection_string, echo=True, pool_pre_ping=True) # Check connections before using them


def get_session():
    with Session(engine) as session:
        yield session