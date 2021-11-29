import os

from app import engine, Base

os.remove('test.db')
Base.metadata.create_all(engine)
