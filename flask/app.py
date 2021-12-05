import enum
from contextlib import contextmanager

from flask import Flask, render_template, request

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Numeric, Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_URL = f'sqlite:///test.db'
engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)
@contextmanager
def session_scope(*args, **kwargs):
    session = session_maker(*args, **kwargs)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

Base = declarative_base()

class BikeType(enum.Enum):
    road = 'Road'
    mountain = 'Mountain'
    electric = 'Electric'
    snow = 'Snow'
    tandem = 'Tandem'

class GearingType(enum.Enum):
    multi_speed = 'Multi-Speed'
    single_speed = 'Single Speed'
    fixed_gear = 'Fixed Gear'
    igh = 'Internal Geared Hub'

class Bike(Base):
    __tablename__ = 'bikes'

    id_ = Column('id', Integer, primary_key=True)
    name = Column(String)
    color = Column(String)
    weight = Column(Numeric)
    type_ = Column('type', Enum(BikeType))
    gearing = Column(Enum(GearingType))
    price = Column(Integer)

app = Flask(__name__)

@app.route('/')
def index():
    with session_scope() as session:
        bikes = session.query(Bike).all()

        return render_template('index.html', bikes=bikes)

@app.route('/add', methods=['GET', 'POST'])
def add_bike():
    if request.method == 'GET':
        return render_template('add_bike.html')
    else:
        form_data = request.form
        print(form_data)
        new_bike = Bike(name=form_data['name'],
                        color=form_data['color'],
                        weight=float(form_data['weight']),
                        type_=getattr(BikeType, form_data['type']),
                        gearing=getattr(GearingType, form_data['gearing']),
                        price=int(float(form_data['price']) * 100))

        with session_scope() as session:
            session.add(new_bike)
            session.commit()

        return index()

@app.route('/delete/<int:id_>', methods=['GET'])
def delete_bike(id_):
    with session_scope() as session:
        bike = session.query(Bike).get(id_)
        if bike is not None:
            session.delete(bike)
            session.commit()
    return index()


@app.context_processor
def inject_enums():
    return {'bike_type': BikeType,
            'gearing_type': GearingType}
