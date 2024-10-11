from models.enclosures import Enclosures

def test_get_all_enclosures(client, add_sample_enclosures):

    response = client.get('/enclosures')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json == [
        {
            "id": 1,
            "location": "Zona 1",
            "name": "Kandang 1"
        },
        {
            "id": 2,
            "location": "Zona 1",
            "name": "Kandang 2"
        }
    ]

def test_post_new_enclosure(client, appjson, test_db):
    new_enclosure = {
        "name": "Kandang Anjing",
        "location": "Zona 1"
    }

    response = client.post('/enclosures', json=new_enclosure, headers=appjson)
    response_json = response.get_json()
    assert response.status_code == 201
    assert response_json['message'] == 'Success add new enclosure'
    assert response_json['enclosures'] == {
        "id": 1,
        "name": "Kandang Anjing",
        "location": "Zona 1"
    }

    enclosure_id = response_json['enclosures']['id']
    enclosure = test_db.session.get(Enclosures, enclosure_id)
    assert enclosure_id == enclosure.id
    assert response_json['enclosures']['name'] == enclosure.name


def test_post_new_enclosure_invalid_data(client, appjson):
    new_enclosure = {
        "location": "Zona 1"
    }

    response = client.post('/enclosures', json=new_enclosure, headers=appjson)
    response_json = response.get_json()

    assert response.status_code == 400
    assert response_json['error'] == "Invalid or Missing field: name"


def test_get_enclosure_by_id(client, add_sample_enclosures):
    print(Enclosures.query.all())
    response = client.get('/enclosures/1')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json == {
        "id": 1,
        "name": "Kandang 1",
        "location": "Zona 1"
    }

def test_get_enclosure_by_id_not_found(client, add_sample_enclosures):
    response = client.get('/enclosures/99')
    response_json = response.get_json()

    assert response.status_code == 404
    assert response_json['message'] == 'Enclosure is not found'

def test_update_enclosure(client, appjson, add_sample_enclosures, test_db):
    updated_enclosure = {
        "name": "Kandang Anjing",
        "location": "Zona 1"
    }

    response = client.put('/enclosures/1', headers=appjson, json=updated_enclosure)
    response_json = response.get_json()

    assert response.status_code == 201
    assert response_json['message'] == 'Success update enclosure'
    assert response_json['enclosures'] == {
        "id": 1,
        "name": "Kandang Anjing",
        "location": "Zona 1"
    }

    enclosure_id = response_json['enclosures']['id']
    enclosure = test_db.session.get(Enclosures, enclosure_id)
    assert enclosure_id == enclosure.id
    assert response_json['enclosures']['name'] == enclosure.name


def test_delete_enclosure(client, add_sample_enclosures, test_db):
    response = client.delete('/enclosures/1')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json['message'] == 'Success delete enclosure'

    deleted_enclosure = test_db.session.get(Enclosures, 1)
    assert deleted_enclosure == None