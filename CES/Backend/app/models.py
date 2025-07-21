from flask_login import UserMixin
from app import db, login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'student', 'lecturer', 'admin', 'responder'
    responder_type = db.Column(db.String(20))  # 'police', 'hospital', 'firefighter'
    last_heartbeat = db.Column(db.DateTime)
    phone_number = db.Column(db.String(15))

class EmergencyAlert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float)  # Updated to store latitude
    longitude = db.Column(db.Float)  # Updated to store longitude
    status = db.Column(db.String(20), default='active')
# User loader for Flask-Login
