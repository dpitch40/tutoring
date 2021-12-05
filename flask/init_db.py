import os
import os.path

from app import engine, Base

if os.path.isfile('test.db'):
    os.remove('test.db')
Base.metadata.create_all(engine)
