from flask import jsonify
from datetime import datetime

def validate_JSON_animals(data):
    validation_schema = {
        'name': str,
        'species': str,
        'age': int,
        'gender': str,
        'special_req': str,
    }

    for key, key_type in validation_schema.items():
        if key not in data or not isinstance(data[key], key_type):
            return False, f"Invalid or missing field: {key}"
        
    return True, None

def validate_JSON_employees(data):
    validation_schema = {
        'name': str, 
        'role': str, 
        'start_schedule': str,
        'end_schedule': str,
    }

    for key, key_type in validation_schema.items():
        if key not in data or not isinstance(data[key], key_type):
            return False, f"Invalid or missing field: {key}"
        
    return True, None

def validate_date(date):
    try:
        datetime.strptime(date, "%d-%m-%Y %H:%M:%S")
        return True, None
    except ValueError:
        return False, "Incorrect datetime format, should be DD-MM-YYYY HH:MM:SS"
