from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , Session
from fastapi import HTTPException
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:kira@localhost/microUser"

engine = create_engine(DATABASE_URL , echo=True)

sessionLocal = sessionmaker(bind=engine , autoflush=False ,autocommit=False)

Base = declarative_base()


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()   
      
   