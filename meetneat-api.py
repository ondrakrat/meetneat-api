from flask import Flask, request, abort, url_for, make_response
from flask.json import jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Base, User

# DB stuff
engine = create_engine('sqlite:///meetneat.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)
prefix = '/api/v1/'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route(prefix + 'users/<int:id>')
def get_user(id):
    user = session.query(User).get(id)
    if not user:
        abort(400)
    return jsonify(user.serialize)


@app.route(prefix + 'users', methods=['POST'])
def create_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        abort(400)
    user = User(username=username)
    user.hash_password(password)
    session.add(user)
    session.commit()
    return (jsonify(
        user.serialize,
        200,
        {'Location': url_for('get_user', id=user.id, _external=True)}
    ))


@app.route(prefix + 'users', methods=['GET'])
def get_users():
    users = session.query(User).all()
    return jsonify([u.serialize for u in users])


@app.route(prefix + 'users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = session.query(User).get(id)
    if not user:
        abort(400)
    session.delete(user)
    return make_response(
        jsonify(id),
        200
    )


if __name__ == '__main__':
    app.run()
