from flask import Blueprint, jsonify
from flask_login import current_user, login_required
from app.models import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/dashboard')
@login_required
def dashboard():
    return jsonify({
        'id': current_user.id,
        'username': current_user.username,
        'email': current_user.email,
        'role': current_user.role,
        'responder_type': current_user.responder_type,
        'last_heartbeat': current_user.last_heartbeat,
        'phone_number': current_user.phone_number
    })