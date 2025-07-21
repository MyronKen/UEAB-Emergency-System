from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import EmergencyAlert
from flask import Blueprint, render_template
from app import db
from app.models import User, EmergencyAlert

responder_bp = Blueprint('responder', __name__)

@responder_bp.route('/alerts', methods=['GET'])
@login_required
def alerts():
    if current_user.role == 'responder':
        alerts = EmergencyAlert.query.filter_by(status='active').all()
        alert_list = [{'id': a.id, 'user_id': a.user_id, 'timestamp': a.timestamp} for a in alerts]
        return jsonify(alert_list)
    return jsonify({'error': 'Unauthorized'}), 403