# init_db.py
from main import Base, engine

Base.metadata.create_all(bind=engine)
