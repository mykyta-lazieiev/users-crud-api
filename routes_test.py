import json
from app import app


def get_client_data():
    return {"name": "Test", "email": "test@gmail.com", "password": "12345"}


def get_request_headers():
    mimetype = 'application/json'
    return {
        'Content-Type': mimetype,
        'Accept': mimetype
    }


def test_create_user():
    data = json.dumps(get_client_data())
    headers = get_request_headers()
    response = app.test_client().post('/users', data=data, headers=headers)
    assert response.status_code == 200
    assert response.json['data'] is not None


def test_update_user():
    data = json.dumps(get_client_data())
    headers = get_request_headers()
    response = app.test_client().put('/users/1', data=data, headers=headers)
    assert response.status_code == 200


def test_get_users():
    response = app.test_client().get('/users')
    assert response.status_code == 200
    assert len(response.json['data']) > 0


def test_get_user():
    response = app.test_client().get('/users/2')
    assert response.status_code == 200
    assert response.json['data'] is not None


def test_delete_user():
    response = app.test_client().delete('/users/1')
    assert response.status_code == 200
