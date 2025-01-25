from http import HTTPStatus


def test_create_user(client):

    response = client.post(
        '/users/',
        json={
            'username': 'Alice',
            'email': 'alice@example.com',
            'password': 'secret'
        }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
            'id': 1,
            'username': 'Alice',
            'email': 'alice@example.com',
        }


def test_read_user(client):

    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
        'users': [
            {
                'username': 'Alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):

    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.OK

    assert response.json() == {
            'username': 'bob',
            'email': 'bob@example.com',
            'id': 1,
        }


def test_update_invalid_user(client):

    response = client.put(
        '/users/2',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpassword',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {
        "detail": "User not found"
    }


def test_delete_user(client):

    response = client.delete(
        '/users/1'
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}


def test_delete_invalid_user(client):

    response = client.delete(
        '/users/2'
    )

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.json() == {
        "detail": "User not found"
    }
