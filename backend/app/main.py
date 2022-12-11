from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, Path
from sqlalchemy.orm import sessionmaker, Session
from app.core.database import db_engine, get_db
import app.core.crud as crud
import app.models as models
import app.models.schemas as schemas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://192.168.0.128:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def read_root():
    return {"Hello", "World"}

@app.get("/items/{id}")
def get_item(id: int, db: Session = Depends(get_db)):
    db_item = crud.get_item(db=db, item_id=id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not Found")
    return db_item

@app.post("/items/")
def create_item(item: schemas.ItemSchema, db: Session = Depends(get_db)):
    return crud.create_item(db=db, item=item)

@app.post("/items/{id}")
def update_item(item: schemas.ItemSchema, id: int, db: Session = Depends(get_db)):
    db_item = crud.update_item(db=db, item_id=id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not Found")
    return db_item

