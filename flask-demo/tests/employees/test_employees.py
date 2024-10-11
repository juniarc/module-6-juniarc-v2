from models.employees import Employees

def test_get_all_employees(client, add_sample_employees):
    response = client.get('/employees')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json == [
        {
            "end_schedule": "31-10-2024 14:30:00",
            "id": 1,
            "name": "Halim",
            "role": "Casheer",
            "start_schedule": "30-10-2024 14:30:00"
        },
        {
            "end_schedule": "31-10-2024 14:30:00",
            "id": 2,
            "name": "Mahmud",
            "role": "Casheer",
            "start_schedule": "30-10-2024 14:30:00"
        }
]

def test_post_new_employee(client, appjson, test_db):
    new_employee = {
        "end_schedule": "31-10-2024 14:30:00",
        "name": "Halim",
        "role": "Casheer",
        "start_schedule": "30-10-2024 14:30:00"
    }

    response = client.post('/employees', json=new_employee, headers=appjson)
    response_json = response.get_json()

    assert response.status_code == 201
    assert response_json['message'] == 'Success add new employee'
    assert response_json['employees'] == {
        'id': 1,
        "end_schedule": "31-10-2024 14:30:00",
        "name": "Halim",
        "role": "Casheer",
        "start_schedule": "30-10-2024 14:30:00"
    }

    employee_id = response_json['employees']['id']
    employee = test_db.session.get(Employees, employee_id)
    assert employee_id == employee.id
    assert response_json['employees']['name'] == employee.name

def test_post_new_employee_invalid_data(client, appjson):
    new_employee = {
        "end_schedule": "31-10-2024 14:30:00",
        "role": "Casheer",
        "start_schedule": "30-10-2024 14:30:00"
    }

    response = client.post('/employees', json=new_employee, headers=appjson)
    response_json = response.get_json()

    assert response.status_code == 400
    assert response_json['error'] == "Invalid or Missing field: name"


def test_get_employee_by_id(client, appjson, add_sample_employees):
    response = client.get('/employees/1')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json == {
        "id": 1,
        "end_schedule": "31-10-2024 14:30:00",
        "name": "Halim",
        "role": "Casheer",
        "start_schedule": "30-10-2024 14:30:00"
    }

def test_get_employee_by_id_not_found(client, appjson, add_sample_employees):
    response = client.get('/employees/99')
    response_json = response.get_json()

    assert response.status_code == 404
    assert response_json['message'] == 'Employee is not found'

def test_update_animal(client, appjson, add_sample_employees, test_db):
    updated_employee = {
        "end_schedule": "31-10-2024 14:30:00",
        "name": "Mamat",
        "role": "Casheer",
        "start_schedule": "30-10-2024 14:30:00"
    }

    response = client.put('/employees/1', headers=appjson, json=updated_employee)
    response_json = response.get_json()

    assert response.status_code == 201
    assert response_json['message'] == 'Success update employee'
    assert response_json['employees'] == {
        "id": 1,
        "end_schedule": "31-10-2024 14:30:00",
        "name": "Mamat",
        "role": "Casheer",
        "start_schedule": "30-10-2024 14:30:00"
    }

    employee_id = response_json['employees']['id']
    employee = test_db.session.get(Employees, employee_id)
    assert employee_id == employee.id
    assert response_json['employees']['name'] == employee.name

def test_delete_animal(client, add_sample_employees, test_db):
    response = client.delete('/employees/1')
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json['message'] == 'Success delete employee'

    deleted_employee = test_db.session.get(Employees, 1)
    assert deleted_employee == None