from twilio.rest import Client
from app import current_app
from cryptography.fernet import Fernet

def send_sms(to, body):
    account_sid = current_app.config['TWILIO_ACCOUNT_SID']
    auth_token = current_app.config['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    from_ = current_app.config['TWILIO_PHONE_NUMBER']
    message = client.messages.create(
        body=body,
        from_=from_,
        to=to
    )
    return message.sid

# Generate a key (store securely, e.g., in environment variables)
key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_message(message):
    return cipher.encrypt(message.encode()).decode()

def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message.encode()).decode()