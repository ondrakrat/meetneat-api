from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean, or_
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    password_hash = Column(String(64))
    email = Column(String)
    picture = Column(String)


class Request(Base):
    __tablename__ = 'request'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    meal_type = Column(String(50), nullable=False)
    location_string = Column(String)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    meal_time = Column(String)
    filled = Column(Boolean)


class Proposal(Base):
    __tablename__ = 'proposal'
    id = Column(Integer, primary_key=True)
    user_proposed_to = Column(Integer)
    user_proposed_from = Column(Integer)
    request_id = Column(Integer, ForeignKey('request.id'))
    request = relationship(Request)
    filled = Column(Boolean)


class MealDate(Base):
    __tablename__ = 'meal_date'
    id = Column(Integer, primary_key=True)
    user_1 = Column(String, nullable = False)
    user_2 = Column(String, nullable = False)
    restaurant_name = Column(String)
    restaurant_address = Column(String)
    restaurant_picture = Column(String)
    meal_time = Column(String)