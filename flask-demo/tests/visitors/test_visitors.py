from models.visitors import Visitors

def test_get_all_visitors(client, add_sample_visitors):
    response = client.get('/visitors')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json == [
        {
            "id": 1,
            "ticket_type": "Child",
            "event_type": "Weekend day",
            "date": "31-10-2024 14:30:00",
            "feedback": "Positive"
        },
        {
            "id": 2,
            "ticket_type": "Adult",
            "event_type": "Normal day",
            "date": "31-10-2024 14:30:00",
            "feedback": "Positive"
        }
]

def test_post_new_visitor(client, appjson, test_db):
    new_visitor = {
        "ticket_type": "Child",
        "event_type": "Weekend day",
        "date": "31-10-2024 14:30:00",
        "feedback": "Positive"
    }

    response = client.post('/visitors', json=new_visitor, headers=appjson)
    response_json = response.get_json()

    assert response.status_code == 201
    assert response_json['message'] == 'Success add new visitor'
    assert response_json['visitors'] == {
        'id': 1,
        "ticket_type": "Child",
        "event_type": "Weekend day",
        "date": "31-10-2024 14:30:00",
        "feedback": "Positive"
    }

    visitor_id = response_json['visitors']['id']
    visitor = test_db.session.get(Visitors, visitor_id)
    assert visitor_id == visitor.id
    assert response_json['visitors']['ticket_type'] == visitor.ticket_type

def test_post_new_visitor_invalid_data(client, appjson):
    new_visitor = {
        "ticket_type": "Child",
        "event_type": "Weekend day",
        "date": "31-10-2024 14:30:00",
    }

    response = client.post('/visitors', json=new_visitor, headers=appjson)
    response_json = response.get_json()

    assert response.status_code == 400
    assert response_json['error'] == "Invalid or Missing field: feedback"


def test_get_visitor_by_id(client, appjson, add_sample_visitors):
    response = client.get('/visitors/1')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json == {
        "id": 1,
        "ticket_type": "Child",
        "event_type": "Weekend day",
        "date": "31-10-2024 14:30:00",
        "feedback": "Positive"
    }

def test_get_visitor_by_id_not_found(client, appjson, add_sample_visitors):
    response = client.get('/visitors/99')
    response_json = response.get_json()

    assert response.status_code == 404
    assert response_json['message'] == 'Visitor is not found'

def test_update_visitor(client, appjson, add_sample_visitors, test_db):
    updated_visitor = {
        "ticket_type": "Adult",
        "event_type": "Weekend day",
        "date": "31-10-2024 14:30:00",
        "feedback": "Positive"
    }

    response = client.put('/visitors/1', headers=appjson, json=updated_visitor)
    response_json = response.get_json()

    assert response.status_code == 201
    assert response_json['message'] == 'Success update visitor'
    assert response_json['visitors'] == {
        "id": 1,
        "ticket_type": "Adult",
        "event_type": "Weekend day",
        "date": "31-10-2024 14:30:00",
        "feedback": "Positive"
    }

    visitor_id = response_json['visitors']['id']
    visitor = test_db.session.get(Visitors, visitor_id)
    assert visitor_id == visitor.id
    assert response_json['visitors']['ticket_type'] == visitor.ticket_type

def test_delete_visitor(client, add_sample_visitors, test_db):
    response = client.delete('/visitors/1')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json['message'] == 'Success delete visitor'

    deleted_visitor = test_db.session.get(Visitors, 1)
    assert deleted_visitor == None