from sqlalchemy.orm import Session
import app.models as models
import app.models.schemas as schemas

def get_item(db:Session, item_id: int):
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_item(db: Session, item: schemas.ItemSchema):
    db_item = models.Item(name=item.name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item_id: int, item: schemas.ItemSchema):
    db_item = get_item(db=db, item_id=item_id)
    if db_item is not None:
        db_item.name = item.name
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db=db, item_id=item_id)
    if db_item is not None:
        db.delete(db_item)
        db.commit()
    return db_item