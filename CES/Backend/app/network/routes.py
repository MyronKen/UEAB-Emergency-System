from flask import Blueprint, jsonify
from flask_login import current_user, login_required

network_bp = Blueprint('network', __name__)

@network_bp.route('/manage', methods=['GET'])
@login_required
def manage_network():
    if current_user.role == 'admin':
        # Mock network management
        return jsonify({'message': 'Network management page'})
    return jsonify({'error': 'Unauthorized'}), 403