from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from logger import execution


DATABASE_URL="mysql+pymysql://root:root@localhost:3306/request_db_fastapi"

engine=create_engine(
    DATABASE_URL
)

sessionlocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base=declarative_base()

def get_db():

    execution.append("Dependency Started (get_db)")

    db = sessionlocal()

    execution.append("Database Session Created")

    try:
        yield db

    finally:
        execution.append("Closing Database Session")
        db.close()
