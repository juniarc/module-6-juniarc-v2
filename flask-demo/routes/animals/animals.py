from flask import jsonify, request, Blueprint

from dataDummy.dataDummy import animal_db
from utils.validation import validate_JSON_animals
from utils.responseMessages import SUCCES_MESSAGES, ERROR_MESSAGES

animals_bp = Blueprint('animals', __name__)

def create_animal(req_data):
    special_req = req_data.get('special_req')
    if special_req == "" :
        special_req = "None"

    return {
        'id': animal_db[-1]['id'] + 1,
        'name': req_data.get('name'),
        'species': req_data.get('species'),
        'age': req_data.get('age'),
        'gender': req_data.get('gender'),
        'special_req': special_req,
    }

def update_animal(animal, req_data):
    special_req = req_data.get('special_req')
    if special_req == "" :
        special_req = "None"

    animal.update({
        'name': req_data.get('name'),
        'species': req_data.get('species'),
        'age': req_data.get('age'),
        'gender': req_data.get('gender'),
        'special_req': special_req,
    })

    return animal

def validate_animal_data(req_data):
    if not req_data:
        return False, ERROR_MESSAGES['json_required']
    
    is_data_valid, error_massage = validate_JSON_animals(req_data)
    if not is_data_valid:
        return jsonify({ 'error': error_massage}), 400
    
    return True, None

@animals_bp.route('', methods=['GET', 'POST'])
def get_all_animals():
    if request.method == 'GET':
        return jsonify(animal_db), 200
    
    elif request.method == 'POST':
        req_data = request.json

        is_valid, error_messages = validate_animal_data(req_data)
        if not is_valid:
            return jsonify({'error': error_messages}), 400

        new_animal = create_animal(req_data)
        animal_db.append(new_animal)

        return jsonify({
            'message': SUCCES_MESSAGES['success_add_animal'],
        }), 201

@animals_bp.route('/<int:animal_id>', methods=['GET', 'PUT', 'DELETE'])
def get_animal_by_id(animal_id):
    global animal_db
    animal = next((animal for animal in animal_db if animal_id == animal['id']), None)
    
    if request.method == 'GET':        
        if animal is None:
            return jsonify({'message': ERROR_MESSAGES['animal_not_found']}), 404
        return jsonify(animal), 200
    
    if request.method == 'PUT':
        req_data = request.json
        
        is_valid, error_messages = validate_animal_data(req_data)
        if not is_valid:
            return jsonify({'error': error_messages}), 400
        
        if animal is None:
            return jsonify({'message': 'Animal is not found'}), 404
        
        updated_animal = update_animal(animal, req_data)

        return jsonify(updated_animal), 201
    
    if request.method == 'DELETE':
        if animal is None:
            return jsonify({'message': 'Animal is not found'}), 404
        
        animal_db = [animal for animal in animal_db if animal['id'] != animal_id]
        return jsonify({"message": "Success delete animal"}), 200