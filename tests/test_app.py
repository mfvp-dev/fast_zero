from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={'username': 'mf', 'email': 'mf@gmail.com', 'password': '1234'},
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'mf',
        'email': 'mf@gmail.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'mf',
                'email': 'mf@gmail.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'mathe',
            'email': 'mf@gmail.com',
            'password': '1234',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'mathe',
        'email': 'mf@gmail.com',
        'id': 1,
    }


def test_delete_user(client):
    reponse = client.delete('/users/1')

    assert reponse.status_code == HTTPStatus.OK
    assert reponse.json() == {'message': 'User deleted'}
