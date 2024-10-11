from flask import jsonify, request, Blueprint

from models.enclosures import Enclosures
from models.feedings import Feedings
from models.animals import Animals
from config.setting import db

from utils.validation import validate_JSON_enclosures
from utils.responseMessages import ERROR_MESSAGES, SUCCES_MESSAGES

enclosures_bp = Blueprint('enclosures', __name__)

def create_enclosure(req_data):
    new_enclosure = Enclosures(
        name = req_data.get('name'),
        location = req_data.get('location'),
    )

    db.session.add(new_enclosure)
    db.session.commit()

    return new_enclosure.to_dict()

def update_enclosure(enclosure, req_data):
    enclosure.name = req_data.get('name')
    enclosure.location = req_data.get('location')

    db.session.commit()

    return enclosure.to_dict()

def delete_enclosure(id):
    enclosure = Enclosures.query.get(id)

    if enclosure is None:
            return jsonify({'message': ERROR_MESSAGES['enclosure_not_found']}), 404
    
    Feedings.query.filter_by(enclosure_id=id).update({'enclosure_id': None})
    Animals.query.filter_by(enclosure_id=id).update({'enclosure_id': None})

    db.session.delete(enclosure)
    db.session.commit()

    return jsonify({"message": SUCCES_MESSAGES['success_delete_enclosure']}), 200

def validate_enclosure_data(req_data):
    if not req_data:
        return False, ERROR_MESSAGES['json_required']
    
    is_data_valid, error_massage = validate_JSON_enclosures(req_data)
    if not is_data_valid:
        return False, error_massage
    
    return True, None

@enclosures_bp.route('', methods=['GET', 'POST'])
def get_all_enclosures():
    if request.method == 'GET':
        enclosures = Enclosures.query.all()
        enclsoures_list = [enclosure.to_dict() for enclosure in enclosures]
        return jsonify(enclsoures_list), 200
    
    elif request.method == 'POST':
        req_data = request.json

        is_valid, error_message = validate_enclosure_data(req_data)
        if not is_valid:
            return jsonify({'error': error_message}), 400
        
        new_enclosure = create_enclosure(req_data)

        return jsonify({
            'message': SUCCES_MESSAGES['success_add_enclosure'],
            'enclosures': new_enclosure
        }), 201

@enclosures_bp.route('/<int:enclosure_id>', methods=['GET', 'PUT', 'DELETE'])
def get_enclosure_by_id(enclosure_id):
    enclosure = Enclosures.query.get(enclosure_id)

    if request.method == 'GET':        
        if enclosure is None:
            return jsonify({'message': ERROR_MESSAGES['enclosure_not_found']}), 404
        return jsonify(enclosure.to_dict()), 200
    
    if request.method == 'PUT':
        req_data = request.json
        
        is_valid, error_messages = validate_enclosure_data(req_data)
        if not is_valid:
            return jsonify({'error': error_messages}), 400
        
        if enclosure is None:
            return jsonify({'message': ERROR_MESSAGES['enclosure_not_found']}), 404
        
        updated_enclosure = update_enclosure(enclosure, req_data)

        return jsonify({
            'message': SUCCES_MESSAGES['success_update_enclosure'],
            'enclosures': updated_enclosure
        }), 201
    
    if request.method == 'DELETE':
        return delete_enclosure(enclosure_id)