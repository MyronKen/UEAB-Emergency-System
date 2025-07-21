from flask import Blueprint, jsonify, request
from flask_login import login_user, logout_user, current_user
from app import db, bcrypt
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get('email')).first()
    if user and bcrypt.check_password_hash(user.password_hash, data.get('password')):
        login_user(user)
        return jsonify({'message': 'Login successful', 'user': {'username': user.username, 'email': user.email, 'role': user.role}}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@auth_bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data.get('password')).decode('utf-8')
    user = User(username=data.get('username'), email=data.get('email'),
                password_hash=hashed_password, role=data.get('role'))
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/forgot_password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    # Placeholder for sending reset email
    return jsonify({'message': 'If an account with that email exists, a password reset link has been sent.'}), 200