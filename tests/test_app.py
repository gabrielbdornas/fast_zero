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
