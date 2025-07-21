from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from config import Config
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import atexit

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Bind extensions to the app
    CORS(app)
    db.init_app(app)
    login_manager.init_app(app)
    bcrypt.init_app(app)

    # Set login view for unauthorized access redirection
    login_manager.login_view = 'auth.login'

    # Register blueprints for modular routing
    from app.auth.routes import auth_bp
    from app.user.routes import user_bp
    from app.wellness.routes import wellness_bp
    from app.emergency.routes import emergency_bp
    from app.communication.routes import communication_bp
    from app.network.routes import network_bp
    from app.responder.routes import responder_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(wellness_bp, url_prefix='/wellness')
    app.register_blueprint(emergency_bp, url_prefix='/emergency')
    app.register_blueprint(communication_bp, url_prefix='/communication')
    app.register_blueprint(network_bp, url_prefix='/network')
    app.register_blueprint(responder_bp, url_prefix='/responder')

    def check_wellness():
        with app.app_context():
            from app.models import User
            from app.utils import send_sms

            now = datetime.utcnow()
            one_hour_ago = now - timedelta(hours=1)
            two_hours_ago = now - timedelta(hours=2)
            
            # Users who haven't checked in the last hour
            inactive_users = User.query.filter(User.last_heartbeat < one_hour_ago).all()
            for user in inactive_users:
                if user.phone_number:
                    send_sms(user.phone_number, "Please check in to confirm your wellness.")
            
            # Users who haven't checked in the last two hours
            critical_users = User.query.filter(User.last_heartbeat < two_hours_ago).all()
            for user in critical_users:
                responders = User.query.filter_by(role='responder').all()
                for responder in responders:
                    if responder.phone_number:
                        send_sms(responder.phone_number, f"User {user.username} has not checked in for over 2 hours.")

    scheduler = BackgroundScheduler()
    scheduler.add_job(check_wellness, 'interval', hours=1)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

    # Initialize the database
    with app.app_context():
        db.create_all() 

    return app
