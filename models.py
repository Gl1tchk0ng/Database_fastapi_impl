import datetime as datetime
from sqlalchemy import Column, Integer, String, Date, DateTime

import database as _database

class Registration(_database.Base):
    __tablename__ = "registration"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    date_of_birth = Column(Date)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)