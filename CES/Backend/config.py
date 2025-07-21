class Config:
    SECRET_KEY = 'your_secret_key_here'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:Qwerty%4055@localhost:3306/UEAB_Emergency_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
    TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
    TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
    TWILIO_API_KEY = 'your_twilio_api_key'
    TWILIO_API_SECRET = 'your_twilio_api_secret'
    TWILIO_APP_SID = 'your_twilio_app_sid'