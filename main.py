from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List
from database import SessionLocal, engine
from database import get_db
import models

# Initialize FastAPI app
app = FastAPI()

# Create tables in the database
models.Base.metadata.create_all(bind=engine)

# Pydantic Models
class PlaceBase(BaseModel):
    name: str
    location_lat: float
    location_long: float
    description: str
    type: str

class PlaceCreate(PlaceBase):
    pass

class Place(PlaceBase):
    id: int

    class Config:
        orm_mode = True

class PhotoBase(BaseModel):
    url: str

class PhotoCreate(PhotoBase):
    pass

class Photo(PhotoBase):
    id: int
    place_id: int

    class Config:
        orm_mode = True

# Inside main.py

# ... Other imports ...



# ... Pydantic models and FastAPI app initialization ...

@app.post("/place/", response_model=Place)
def create_place(place: PlaceCreate, db: Session = Depends(get_db)):
    db_place = models.Place(**place.dict())
    db.add(db_place)
    db.commit()
    db.refresh(db_place)
    return db_place


@app.put("/place/{place_id}/", response_model=Place)
def update_place(place_id: int, place: PlaceCreate, db: Session = Depends(get_db)):
    db_place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not db_place:
        raise HTTPException(status_code=404, detail="Place not found")

    for key, value in place.dict().items():
        setattr(db_place, key, value)

    db.commit()
    db.refresh(db_place)
    return db_place


@app.delete("/place/{place_id}/", response_model=dict)
def delete_place(place_id: int, db: Session = Depends(get_db)):
    db_place = db.query(models.Place).filter(models.Place.id == place_id).first()
    if not db_place:
        raise HTTPException(status_code=404, detail="Place not found")

    db.delete(db_place)
    db.commit()
    return {"message": "Place deleted successfully"}

@app.post("/place/{place_id}/photo/", response_model=Photo)
def add_photo(place_id: int, photo: PhotoCreate, db: Session = Depends(get_db)):
    db_photo = models.Photo(**photo.dict(), place_id=place_id)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo

@app.put("/photo/{photo_id}/", response_model=Photo)
def update_photo(photo_id: int, photo: PhotoCreate, db: Session = Depends(get_db)):
    db_photo = db.query(models.Photo).filter(models.Photo.id == photo_id).first()
    if not db_photo:
        raise HTTPException(status_code=404, detail="Photo not found")

    for key, value in photo.dict().items():
        setattr(db_photo, key, value)

    db.commit()
    db.refresh(db_photo)
    return db_photo

@app.delete("/photo/{photo_id}/", response_model=dict)
def delete_photo(photo_id: int, db: Session = Depends(get_db)):
    db_photo = db.query(models.Photo).filter(models.Photo.id == photo_id).first()
    if not db_photo:
        raise HTTPException(status_code=404, detail="Photo not found")

    db.delete(db_photo)
    db.commit()
    return {"message": "Photo deleted successfully"}

@app.get("/photos/", response_model=List[Photo])
def list_all_photos(db: Session = Depends(get_db)):
    photos = db.query(models.Photo).all()
    return photos


@app.get("/places/", response_model=List[Place])
def list_places(db: Session = Depends(get_db)):
    return db.query(models.Place).all()

@app.post("/place/{place_id}/photo/", response_model=Photo)
def add_photo(place_id: int, photo: PhotoCreate, db: Session = Depends(get_db)):
    db_photo = models.Photo(**photo.dict(), place_id=place_id)
    db.add(db_photo)
    db.commit()
    db.refresh(db_photo)
    return db_photo

@app.get("/place/{place_id}/photos/", response_model=List[Photo])
def list_photos(place_id: int, db: Session = Depends(get_db)):
    return db.query(models.Photo).filter(models.Photo.place_id == place_id).all()
