from flask import jsonify, request, Blueprint
from sqlalchemy import text

from utils.validation import validate_JSON_animals
from utils.responseMessages import SUCCES_MESSAGES, ERROR_MESSAGES
from models.animals import Animals
from config.setting import db

animals_bp = Blueprint('animals', __name__)

def reset_sequence():
    with db.engine.connect() as connection:
        connection.execute(text("ALTER SEQUENCE public.animals_id_seq RESTART WITH 1;"))

def create_animal(req_data):
    special_req = req_data.get('special_req', 'None')

    new_animal = Animals(
        enclosure_id = req_data.get('enclosure_id'),
        name = req_data.get('name'),
        species = req_data.get('species'),
        age = req_data.get('age'),
        gender =  req_data.get('gender'),
        special_req = special_req,
    )

    db.session.add(new_animal)
    db.session.commit()

    return new_animal.to_dict()
    

def update_animal(animal, req_data):
    animal.enclosure_id = req_data.get('enclosure_id')
    animal.name = req_data.get('name')
    animal.species = req_data.get('species')
    animal.age = req_data.get('age')
    animal.gender =  req_data.get('gender')
    animal.special_req = req_data.get('special_req', 'None')

    db.session.commit()

    return animal.to_dict()

def validate_animal_data(req_data):
    if not req_data:
        return False, ERROR_MESSAGES['json_required']
    
    is_data_valid, error_massage = validate_JSON_animals(req_data)
    if not is_data_valid:
        return False, error_massage
    
    return True, None

@animals_bp.route('', methods=['GET', 'POST'])
def get_all_animals():
    if request.method == 'GET':
        animals = Animals.query.all()
        animals_list = [animal.to_dict() for animal in animals]
        return jsonify(animals_list), 200
    
    elif request.method == 'POST':
        req_data = request.json

        is_valid, error_messages = validate_animal_data(req_data)
        if not is_valid:
            return jsonify({'error': error_messages}), 400
        
        if Animals.query.count() == 0:
            reset_sequence()

        new_animal = create_animal(req_data)

        return jsonify({
            'message': SUCCES_MESSAGES['success_add_animal'],
            'animals': new_animal
        }), 201

@animals_bp.route('/<int:animal_id>', methods=['GET', 'PUT', 'DELETE'])
def get_animal_by_id(animal_id):
    animal = Animals.query.get(animal_id)

    if request.method == 'GET':        
        if animal is None:
            return jsonify({'message': ERROR_MESSAGES['animal_not_found']}), 404
        return jsonify(animal.to_dict()), 200
    
    if request.method == 'PUT':
        req_data = request.json
        
        is_valid, error_messages = validate_animal_data(req_data)
        if not is_valid:
            return jsonify({'error': error_messages}), 400
        
        if animal is None:
            return jsonify({'message': ERROR_MESSAGES['animal_not_found']}), 404
        
        updated_animal = update_animal(animal, req_data)

        return jsonify({
            'message': SUCCES_MESSAGES['success_update_animal'],
            'animals': updated_animal
        }), 201
    
    if request.method == 'DELETE':
        if animal is None:
            return jsonify({'message': 'Animal is not found'}), 404
        
        db.session.delete(animal)
        db.session.commit()

        return jsonify({"message": SUCCES_MESSAGES['success_delete_animal']}), 200