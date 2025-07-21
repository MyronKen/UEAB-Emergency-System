# Backend Setup

## Environment Variables
To run the backend server, you need to set up the following environment variables. You can create a `.env` file in the `Backend` directory to store these variables.

```
MYSQL_USER=root
MYSQL_PASSWORD=Qwerty@55
MYSQL_DB=UEAB_Emergency_db
MYSQL_HOST=localhost
MYSQL_PORT=3306

# Twilio Configuration
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=your_twilio_phone_number
TWILIO_API_KEY=your_twilio_api_key
TWILIO_API_SECRET=your_twilio_api_secret
TWILIO_APP_SID=your_twilio_app_sid
```

### Running the Application
Once the environment variables are set, you can install the dependencies and run the application:
```bash
pip install -r requirements.txt
python run.py