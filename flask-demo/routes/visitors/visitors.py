from flask import jsonify, request, Blueprint

from models.visitors import Visitors
from config.setting import db

from utils.validation import validate_JSON_visitors, validate_date
from utils.responseMessages import ERROR_MESSAGES, SUCCES_MESSAGES

visitors_bp = Blueprint('visitors', __name__)

def create_visitor(req_data):
    new_visitor = Visitors(
        event_type = req_data.get('event_type'),
        ticket_type = req_data.get('ticket_type'),
        date = req_data.get('date'),
        feedback =  req_data.get('feedback'),
    )

    db.session.add(new_visitor)
    db.session.commit()

    return new_visitor.to_dict()

def update_visitor(visitor, req_data):
    visitor.event_type =  req_data.get('event_type')
    visitor.ticket_type =  req_data.get('ticket_type')
    visitor.date =  req_data.get('date')
    visitor.feedback =  req_data.get('feedback')

    db.session.commit()

    return visitor.to_dict()

def validate_visitor_data(req_data):
    if not req_data:
        return False, ERROR_MESSAGES['json_required']
    
    is_data_valid, error_massage = validate_JSON_visitors(req_data)
    if not is_data_valid:
        return False, error_massage
    
    is_dateFormat_valid, error_massage = validate_date(req_data.get('date'))
    if not is_dateFormat_valid:
        return False, error_massage
    
    return True, None

@visitors_bp.route('', methods=['GET', 'POST'])
def get_all_visitors():
    if request.method == 'GET':
        visitors = Visitors.query.all()
        visitors_list = [visitor.to_dict() for visitor in visitors]
        return jsonify(visitors_list), 200
    
    elif request.method == 'POST':
        req_data = request.json

        is_valid, error_message = validate_JSON_visitors(req_data)
        if not is_valid:
            return jsonify({'error': error_message}), 400
        
        new_visitor = create_visitor(req_data)

        return jsonify({
            'message': SUCCES_MESSAGES['success_add_visitor'],
            'feeding': new_visitor
        }), 200
    
@visitors_bp.route('/<int:visitor_id>', methods=['GET', 'PUT', 'DELETE'])
def get_visitor_by_id(visitor_id):
    visitor = Visitors.query.get(visitor_id)

    if request.method == 'GET':        
        if visitor is None:
            return jsonify({'message': ERROR_MESSAGES['visitor_not_found']}), 404
        return jsonify(visitor.to_dict()), 200
    
    if request.method == 'PUT':
        req_data = request.json
        
        is_valid, error_messages = validate_visitor_data(req_data)
        if not is_valid:
            return jsonify({'error': error_messages}), 400
        
        if visitor is None:
            return jsonify({'message': ERROR_MESSAGES['visitor_not_found']}), 404
        
        updated_visitor = update_visitor(visitor, req_data)

        return jsonify({
            'message': SUCCES_MESSAGES['success_update_visitor'],
            'animals': updated_visitor
        }), 201
    
    if request.method == 'DELETE':
        if visitor is None:
            return jsonify({'message': ERROR_MESSAGES['visitor_not_found']}), 404
        
        db.session.delete(visitor)
        db.session.commit()

        return jsonify({"message": SUCCES_MESSAGES['success_delete_visitor']}), 200
