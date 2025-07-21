from flask import Blueprint, request, jsonify
from flask_login import current_user, login_required
from app import db
from app.models import EmergencyAlert
from datetime import datetime

emergency_bp = Blueprint('emergency', __name__)

@emergency_bp.route('/panic', methods=['POST'])
@login_required
def panic():
    if current_user.role in ['student', 'lecturer']:
        data = request.get_json()
        alert = EmergencyAlert(
            user_id=current_user.id,
            timestamp=datetime.utcnow(),
            latitude=data.get('latitude'),
            longitude=data.get('longitude')
        )
        db.session.add(alert)
        db.session.commit()
        # Placeholder for broadcasting alert
        return jsonify({'message': 'Emergency alert sent successfully!'})
    return jsonify({'error': 'Unauthorized'}), 403
