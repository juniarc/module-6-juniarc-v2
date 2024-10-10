from flask import jsonify, request, Blueprint

# from dataDummy.dataDummy import employee_db
from utils.validation import validate_JSON_employees, validate_date
from utils.responseMessages import ERROR_MESSAGES, SUCCES_MESSAGES
from models.employees import Employees
from config.setting import db

employee_bp = Blueprint('employees', __name__)

def create_employee(req_data):
    new_employee = Employees(
        name= req_data.get('name'),
        role= req_data.get('role'),
        start_schedule= req_data.get('start_schedule'),
        end_schedule= req_data.get('end_schedule'),
    )

    db.session.add(new_employee)
    db.session.commit()

    return new_employee.to_dict()

def update_employee(employee, req_data):
    employee.name= req_data.get('name'),
    employee.role= req_data.get('role'),
    employee.start_schedule= req_data.get('start_schedule'),
    employee.end_schedule= req_data.get('end_schedule'),
    
    db.session.commit()

    return employee.to_dict()

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
        employees = Employees.query.all()
        employee_list = [employee.to_dict() for employee in employees]
        return jsonify(employee_list), 200
    
    elif request.method == 'POST':
        req_data = request.json

        is_valid, error_message = validate_employee_data(req_data)
        if not is_valid:
            return jsonify({'error': error_message}), 400

        new_employee = create_employee(req_data)

        return jsonify({
            'message': SUCCES_MESSAGES['success_add_employee'],
            'employees': new_employee
        }), 201

@employee_bp.route('/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def get_employee_by_id(employee_id):
    employee = Employees.query.get(employee_id)

    if request.method == 'GET':        
        if employee is None:
            return jsonify({'message': ERROR_MESSAGES['employee_not_found']}), 404
        return jsonify(employee.to_dict()), 200
    
    if request.method == 'PUT':
        req_data = request.json
        
        is_valid, error_message = validate_employee_data(req_data)
        if not is_valid:
            return jsonify({'error': error_message}), 400
        
        if employee is None:
            return jsonify({'message': ERROR_MESSAGES['employee_not_found']}), 404
        
        updated_employee = update_employee(employee, req_data)

        return jsonify({
            'message': SUCCES_MESSAGES['success_update_employee'],
            'animals': updated_employee
        }), 201
    
    if request.method == 'DELETE':
        if employee is None:
            return jsonify({'message': ERROR_MESSAGES['employee_not_found']}), 404
        
        db.session.delete(employee)
        db.session.commit()

        return jsonify({"message": SUCCES_MESSAGES['success_delete_employee']}), 200