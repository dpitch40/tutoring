from contextlib import contextmanager

from flask import Flask

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = f"sqlite:///test.db"
engine = create_engine(DB_URL)
session = sessionmaker(bind=engine)
@contextmanager
def session_scope(*args, **kwargs):
    session = session(*args, **kwargs)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

Base = declarative_base()

class Car(Base):
    __tablename__ = 'cars'

    id_ = Column("id", Integer, primary_key=True)
    speed = Column(Integer)
    color = Column(String)

app = Flask(__name__)

@app.route("/")
def hello_world():
    with session_scope() as session:
        return "<p>Hello, World!</p>"
