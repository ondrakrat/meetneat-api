from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base

# DB stuff
engine = create_engine('sqlite:///meetneat.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
