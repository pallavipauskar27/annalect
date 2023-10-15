from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Place(Base):
    __tablename__ = "places"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location_lat = Column(Float)
    location_long = Column(Float)
    description = Column(String)
    type = Column(String)
    photos = relationship("Photo", back_populates="place")

class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    place_id = Column(Integer, ForeignKey('places.id'))
    place = relationship("Place", back_populates="photos")
