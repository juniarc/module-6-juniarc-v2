from flask import jsonify, request, Blueprint
from sqlalchemy import text

from models.feedings import Feedings
from models.animals import Animals
from models.enclosures import Enclosures
from config.setting import db

from utils.validation import validate_JSON_feedings, validate_date
from utils.responseMessages import ERROR_MESSAGES, SUCCES_MESSAGES

feedings_bp = Blueprint('feedings', __name__)

def create_feeding(req_data):
    new_feeding = Feedings(
        animal_id = req_data.get('animal_id'),
        enclosure_id = req_data.get('enclosure_id'),
        food_type = req_data.get('food_type'),
        feeding_time =  req_data.get('feeding_time'),
        reminder =  req_data.get('reminder'),
    )

    db.session.add(new_feeding)
    db.session.commit()

    return new_feeding.to_dict()


def validate_feeding_data(req_data):
    if not req_data:
        return False, ERROR_MESSAGES['json_required']
    
    is_data_valid, error_massage = validate_JSON_feedings(req_data)
    if not is_data_valid:
        return False, error_massage
        
    animal_id = req_data.get('animal_id')
    animal = Animals.query.get(animal_id)
    if animal is None:
        return False, ERROR_MESSAGES['animal_id_not_found']

    enclosure_id = req_data.get('enclosure_id')
    enclosure = Enclosures.query.get(enclosure_id)
    if enclosure is None:
        return False, ERROR_MESSAGES['enclosure_id_not_found']
    
    is_dateFormat_feeding_time_valid, error_massage_feeding_time = validate_date(req_data.get('feeding_time'))
    if not is_dateFormat_feeding_time_valid:
        return False, error_massage_feeding_time
    
    is_dateFormat_reminder, error_massage_reminder = validate_date(req_data.get('reminder'))
    if not is_dateFormat_reminder:
        return False, error_massage_reminder
    
    return True, None

@feedings_bp.route('', methods=['GET', 'POST'])
def get_all_feedings():
    if request.method == 'GET':
        feedings = Feedings.query.all()
        feedings_list = [feeding.to_dict() for feeding in feedings]
        return jsonify(feedings_list), 200
    
    elif request.method == 'POST':
        req_data = request.json

        is_valid, error_message = validate_feeding_data(req_data)
        if not is_valid:
            return jsonify({'error': error_message}), 400
        
        new_feeding = create_feeding(req_data)

        return jsonify({
            'message': SUCCES_MESSAGES['success_add_feeding'],
            'feeding': new_feeding
        }), 200

@feedings_bp.route('/<int:feeding_id>', methods=['GET', 'PUT', 'DELETE'])
def get_feeding_by_id(feeding_id):
    feeding = Feedings.query.get(feeding_id)

    if request.method == 'GET':        
        if feeding is None:
            return jsonify({'message': ERROR_MESSAGES['feeding_not_found']}), 404
        return jsonify(feeding.to_dict()), 200
    
    if request.method == 'PUT':
        req_data = request.json
        
        is_valid, error_messages = validate_feeding_data(req_data)
        if not is_valid:
            return jsonify({'error': error_messages}), 400
        
        if feeding is None:
            return jsonify({'message': ERROR_MESSAGES['feeding_not_found']}), 404
        
        updated_feeding = updated_feeding(feeding, req_data)

        return jsonify({
            'message': SUCCES_MESSAGES['success_update_feeding'],
            'animals': updated_feeding
        }), 201
    
    if request.method == 'DELETE':
        if feeding is None:
            return jsonify({'message': ERROR_MESSAGES['feeding_not_found']}), 404
        
        db.session.delete(feeding)
        db.session.commit()

        return jsonify({"message": SUCCES_MESSAGES['success_delete_feeding']}), 200
