from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean, or_
from sqlalchemy.orm import relationship
from passlib.apps import custom_app_context as pwd_context

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))
    email = Column(String)
    picture = Column(String)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'picture': self.picture
        }


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
    user_1 = Column(String, nullable=False)
    user_2 = Column(String, nullable=False)
    restaurant_name = Column(String)
    restaurant_address = Column(String)
    restaurant_picture = Column(String)
    meal_time = Column(String)
