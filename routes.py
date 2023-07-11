from flask import jsonify, request
from app import app
from repository import UsersRepository

repository = UsersRepository()


@app.route("/users")
def fetch_users():
    result = repository.fetch_all()
    result = [tuple(row) for row in result]
    return jsonify({
        'message': 'Users list',
        'data': list(result)
    })


@app.route("/users/<id>")
def get_user(id):
    result = repository.get_user(id)
    return jsonify({
        'message': 'User data',
        'data': result if result is None else dict(result)
    })


@app.route("/users", methods=['POST'])
def create_user():
    id = repository.create_user(request.json)
    result = repository.get_user(id)
    return jsonify({
        'message': 'User created',
        'data': dict(result)
    })


@app.route("/users/<id>", methods=['PUT'])
def edit_user(id):
    repository.edit_user(id, request.json)
    return jsonify({
        'message': 'User updated'
    })


@app.route("/users/<id>", methods=['DELETE'])
def delete_user(id):
    repository.delete_user(id)
    return jsonify({
        'message': 'User deleted'
    })
