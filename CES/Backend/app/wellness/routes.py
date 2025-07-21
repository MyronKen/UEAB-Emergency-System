from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from app import db
from app.models import User
from datetime import datetime

wellness_bp = Blueprint('wellness', __name__)

@wellness_bp.route('/checkin', methods=['POST'])
@login_required
def checkin():
    if current_user.role in ['student', 'lecturer']:
        data = request.get_json()
        current_user.last_heartbeat = datetime.utcnow()
        current_user.latitude = data.get('latitude')
        current_user.longitude = data.get('longitude')
        db.session.commit()
        return jsonify({'message': 'Check-in successful'})
    return jsonify({'error': 'Unauthorized'}), 403

wellness_bp = Blueprint('wellness', __name__)

@wellness_bp.route('/checkin', methods=['POST'])
@login_required
def checkin():
    if current_user.role in ['student', 'lecturer']:
        current_user.last_heartbeat = datetime.utcnow()
        db.session.commit()
        return jsonify({'message': 'Check-in successful'})
    return jsonify({'error': 'Unauthorized'}), 403

@wellness_bp.route('/status', methods=['GET'])
@login_required
def status():
    if current_user.role in ['admin', 'responder']:
        users = User.query.filter(User.role.in_(['student', 'lecturer'])).all()
        status_list = [{'username': u.username, 'last_heartbeat': u.last_heartbeat} for u in users]
        return jsonify(status_list)
    return jsonify({'error': 'Unauthorized'}), 403