from sqlalchemy import (
    Column, Integer, DateTime,
    String
)
from sqlalchemy.sql import func
from . import db, Model


class Product(db.Model, Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    price = Column(Integer, nullable=False, default=0)
    time_created = Column(DateTime, server_default=func.now())
    time_updated = Column(DateTime, server_onupdate=func.now())
