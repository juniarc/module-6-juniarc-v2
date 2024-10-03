from flask import jsonify, request, Blueprint

from dataDummy.dataDummy import employee_db
from utils.validation import validate_JSON_employees, validate_date
from utils.responseMessages import ERROR_MESSAGES, SUCCES_MESSAGES

employee_bp = Blueprint('employees', __name__)

def create_employee(req_data):
    return {
        'id': employee_db[-1]['id'] + 1,
        'name': req_data.get('name'),
        'role': req_data.get('role'),
        'start_schedule': req_data.get('start_schedule'),
        'end_schedule': req_data.get('end_schedule'),
    }

def update_employee(employee, req_data):
    employee.update({
        'name': req_data.get('name'),
        'role': req_data.get('role'),
        'start_schedule': req_data.get('start_schedule'),
        'end_schedule': req_data.get('end_schedule'),
    })

    return employee

def validate_employee_data(req_data):

    if not req_data:
        return False, ERROR_MESSAGES['json_required']

    is_data_valid, error_massage_JSON = validate_JSON_employees(req_data)
    if not is_data_valid:
        return False, error_massage_JSON
    
    is_dateFormat_start_valid, error_massage_start_date = validate_date(req_data.get('start_schedule'))
    if not is_dateFormat_start_valid:
        return False, error_massage_start_date
    
    is_dateFormat_end_valid, error_massage_end_date = validate_date(req_data.get('end_schedule'))
    if not is_dateFormat_end_valid:
        return False, error_massage_end_date
    
    return True, None

@employee_bp.route('', methods=['GET', 'POST'])
def get_all_employees():
    if request.method == 'GET':
        return jsonify(employee_db), 200
    
    if request.method == 'POST':
        req_data = request.json

        is_valid, error_message = validate_employee_data(req_data)
        if not is_valid:
            return jsonify({'error': error_message}), 400

        new_employee = create_employee(req_data)
        employee_db.append(new_employee)

        return jsonify({
            'message': SUCCES_MESSAGES['success_add_employee'],
        }), 201

@employee_bp.route('/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def get_employee_by_id(employee_id):
    global employee_db
    employee = next((employee for employee in employee_db if employee_id == employee['id']), None)
    
    if request.method == 'GET':        
        if employee is None:
            return jsonify({'message': ERROR_MESSAGES['employee_not_found']}), 404
        return jsonify(employee), 200
    
    if request.method == 'PUT':
        req_data = request.json
        
        is_valid, error_message = validate_employee_data(req_data)
        if not is_valid:
            return jsonify({'error': error_message}), 400
        
        if employee is None:
            return jsonify({'message': ERROR_MESSAGES['employee_not_found']}), 404
        
        updated_employee = update_employee(employee, req_data)

        return jsonify(updated_employee), 201
    
    if request.method == 'DELETE':
        if employee is None:
            return jsonify({'message': ERROR_MESSAGES['employee_not_found']}), 404
        
        employee_db = [employee for employee in employee_db if employee['id'] != employee_id]
        return jsonify({"message": SUCCES_MESSAGES['success_delete_employee']}), 200