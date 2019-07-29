# model.py
 
from sqlalchemy import Table, Column, create_engine
from sqlalchemy import Integer, ForeignKey, String, Unicode, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relation
import datetime

engine = create_engine("sqlite:///devdata.db", echo=True)
DeclarativeBase = declarative_base(engine)
metadata = DeclarativeBase.metadata

class Event(DeclarativeBase):
    """"""
    __tablename__ = "event"
 
    id         = Column(Integer, primary_key=True)
    link = Column("link", String(500))
    judul  = Column("judul", String(100))
    timestamp = Column(DateTime, 
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now())

    waktu_event = Column(
        "waktu_event", DateTime
    )    
    waktu_berlangsung = Column(
        "waktu_berlangsung", DateTime
    )    
    status = Column("status_posting", Integer)
 
metadata.create_all()