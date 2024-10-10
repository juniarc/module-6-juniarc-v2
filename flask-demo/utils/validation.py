from flask import jsonify
from datetime import datetime

def validate_JSON_request(data, validation_schema):
    for key, key_type in validation_schema.items():
    
        if key not in data:
            return False, f"Invalid or Missing field: {key}"
        
        if not isinstance(data[key], key_type):
            return False, f"Invalid type for field: {key}. Expected {key_type.__name__}, got {type(data[key]).__name__}"
                
    return True, None

def validate_JSON_animals(data):
    validation_schema = {
        'name': str,
        'enclosure_id': int,
        'species': str,
        'age': int,
        'gender': str,
        'special_req': str,
    }

    is_valid = validate_JSON_request(data, validation_schema)

    return is_valid

def validate_JSON_employees(data):
    validation_schema = {
        'name': str, 
        'role': str, 
        'start_schedule': str,
        'end_schedule': str,
    }

    is_valid = validate_JSON_request(data, validation_schema)
    return is_valid

def validate_JSON_feedings(data):
    validation_schema = {
        'animal_id': int, 
        'enclosure_id': int, 
        'food_type': str,
        'feeding_time': str,
        'reminder': str,
    }

    is_valid = validate_JSON_request(data, validation_schema)

    return is_valid

def validate_JSON_enclosures(data):
    validation_schema = {
        'name': str,
        'location': str
    }
    is_valid = validate_JSON_request(data, validation_schema)

    return is_valid

def validate_JSON_visitors(data):
    validation_schema = {
        'ticket_type': str,
        'event_type': str,
        'date': str,
        'feedback': str
    }

    is_valid = validate_JSON_request(data, validation_schema)

    return is_valid

def validate_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y %H:%M:%S")
        return True, None
    except ValueError:
        return False, "Incorrect datetime format, should be DD-MM-YYYY HH:MM:SS"
