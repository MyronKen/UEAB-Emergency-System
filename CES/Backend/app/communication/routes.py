from flask import Blueprint, request, jsonify
from twilio.twiml.voice_response import VoiceResponse
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from config import Config

communication_bp = Blueprint('communication', __name__)

@communication_bp.route('/token')
def token():
    """Generate a Twilio access token."""
    account_sid = Config.TWILIO_ACCOUNT_SID
    api_key = Config.TWILIO_API_KEY
    api_secret = Config.TWILIO_API_SECRET
    outgoing_application_sid = Config.TWILIO_APP_SID
    identity = 'user' # In a real app, this would be the logged-in user's ID or username

    access_token = AccessToken(account_sid, api_key, api_secret, identity=identity)

    voice_grant = VoiceGrant(
        outgoing_application_sid=outgoing_application_sid,
        incoming_allow=True, # Allow incoming calls
    )
    access_token.add_grant(voice_grant)

    return jsonify(token=access_token.to_jwt())

@communication_bp.route('/message', methods=['POST'])
def send_message():
    # Mock sending a message
    return jsonify({'message': 'Message sent'})

@communication_bp.route('/voip', methods=['POST'])
def initiate_voip():
    """Generate TwiML for a VoIP call."""
    response = VoiceResponse()
    # Replace with the actual responder's number
    response.dial('+15551234567')
    return str(response), 200, {'Content-Type': 'text/xml'}