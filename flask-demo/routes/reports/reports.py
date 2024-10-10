from flask import Blueprint, jsonify
from sqlalchemy import text

from config.setting import db
from models.animals import Animals

reports_bp = Blueprint('reports',__name__)

@reports_bp.route('/animals', methods=['GET'])
def get_animals_report():
    query = text("""
        SELECT species, gender, enclosure_id, COUNT(*) as count
        FROM animals
        GROUP BY species, gender, enclosure_id;
    """)
    results = db.session.execute(query).fetchall()

    report = [{'species': row[0], 'gender': row[1], 'enclosure_id': row[2], 'count': row[3]} for row in results]

    return jsonify(report), 200

@reports_bp.route('/visitors', methods=['GET'])
def get_visitors_report():
    query = text("""
        SELECT event_type, ticket_type, feedback, date, COUNT(*) as count
        FROM visitors
        GROUP BY event_type, ticket_type, feedback, date;
    """)

    results = db.session.execute(query).fetchall()

    report = [{'event_type': row[0], 'ticket_type': row[1], 'feedback': row[2], 'date': row[3], 'count': row[4]} for row in results]

    return jsonify(report), 200

@reports_bp.route('/revenue', methods=['GET'])
def get_revenue_report():
    price_mapping = {
        ('Normal day', 'Adult'): 30,
        ('Normal day', 'Child'): 15,
        ('Weekend day', 'Adult'): 50,
        ('Weekend day', 'Child'): 25,
        ('Special event', 'Adult'): 100,
        ('Special event', 'Child'): 50
    }

    query = text("""
        SELECT event_type, ticket_type, COUNT(*) as count
        FROM visitors
        GROUP BY event_type, ticket_type;
    """)

    results = db.session.execute(query).fetchall()

    report = []

    for row in results:
        event_type = row[0]
        ticket_type = row[1]
        count = row[2]

        price = price_mapping.get((event_type, ticket_type), 0)
        print(event_type)
        revenue = price * count

        report.append({
            'event_type': event_type,
            'ticket_type': ticket_type,
            'revenue': revenue
        })

    return jsonify(report), 200