from models.animals import Animals

def test_get_all_animals(client, add_sample_enclosures, add_sample_animals):
    """Test test_get_all_animals func to ensure get response all animals"""

    response = client.get('/animals')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json == [
        {
            'id': 1,
            'enclosure_id': 1,
            'name': 'Ujang',
            'species': 'Cat',
            'age': 1,
            'gender': 'Male',
            'special_req': 'None'
        },
        {
            'id': 2,
            'enclosure_id': 2,
            'name': 'Onyet',
            'species': 'Cat',
            'age': 1,
            'gender': 'Female',
            'special_req': 'None'
        }
    ]

def test_post_new_animal(client, appjson, add_sample_enclosures, test_db):
    new_animal = {
        "age": 1,
        "enclosure_id": 1,
        "gender": "Male",
        "name": "Dogy",
        "special_req": "None",
        "species": "Dog"
    }

    response = client.post('/animals', json=new_animal, headers=appjson)
    response_json = response.get_json()

    assert response.status_code == 201
    assert response_json['message'] == 'Success add new animal'
    assert response_json['animals'] == {
        "id": 1,
        "age": 1,
        "enclosure_id": 1,
        "gender": "Male",
        "name": "Dogy",
        "special_req": "None",
        "species": "Dog"
    }
    animal_id = response_json['animals']['id']
    animal = test_db.session.get(Animals, animal_id)
    assert animal_id == animal.id
    assert response_json['animals']['name'] == animal.name

def test_post_new_animal_invalid_data(client, appjson, add_sample_enclosures):
    new_animal = {
        "enclosure_id": 1,
        "gender": "Male",
        "name": "Dogy",
        "special_req": "None",
        "species": "Dog"
    }

    response = client.post('/animals', json=new_animal, headers=appjson)
    response_json = response.get_json()

    assert response.status_code == 400
    assert response_json['error'] == "Invalid or Missing field: age"


def test_get_animal_by_id(client, appjson, add_sample_enclosures, add_sample_animals):
    response = client.get('/animals/1')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json == {
        'id':1,
        'enclosure_id':1,
        'name': "Ujang",
        'species': "Cat",
        'age': 1,
        'gender': "Male",
        'special_req':"None"
    }

def test_get_animal_by_id_not_found(client, appjson, add_sample_enclosures, add_sample_animals):
    response = client.get('/animals/3')
    response_json = response.get_json()

    assert response.status_code == 404
    assert response_json['message'] == 'Animal is not found'

def test_update_animal(client, appjson, add_sample_enclosures, add_sample_animals, test_db):
    updated_animal = {
        "enclosure_id": 1,
        "name": "Ujang",
        "species": "Dog",
        "age": 2,
        "gender": "Male",
        "special_req": "None"
    }

    response = client.put('/animals/1', headers=appjson, json=updated_animal)
    response_json = response.get_json()

    assert response.status_code == 201
    assert response_json['message'] == 'Success update animal'
    assert response_json['animals'] == {
        'id': 1,
        "enclosure_id": 1,
        "name": "Ujang",
        "species": "Dog",
        "age": 2,
        "gender": "Male",
        "special_req": "None"
    }

    animal_id = response_json['animals']['id']
    animal = test_db.session.get(Animals, animal_id)
    assert animal_id == animal.id
    assert response_json['animals']['name'] == animal.name


def test_delete_animal(client, add_sample_enclosures, add_sample_animals, test_db):
    response = client.delete('/animals/1')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json['message'] == 'Success delete animal'

    deleted_animal = test_db.session.get(Animals, 1)
    assert deleted_animal == None