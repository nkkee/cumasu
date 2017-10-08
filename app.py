import os
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from pyrebase import pyrebase
 
# settings.py
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OR, the same with increased verbosity:
#load_dotenv(dotenv_path, verbose=True)

app = Flask(__name__)
print(os.environ['test'])
# Find these values at https://twilio.com/user/account
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
 
 
@app.route("/", methods=['POST'])
def receive_order():
    message = client.messages.create(
        to=os.environ['PHONE_NUMBER'],
        from_=os.environ['TWILIO_NUMBER'],
        body="Welcome to Cumasu")
    
    return '', 200

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()


    config = {
      "apiKey": "AIzaSyBg0TlfTsH8qjIU8VnmNJ8rTb8e5TK8b0c",
      "authDomain": "cumasu-1.firebaseapp.com",
      "databaseURL": "https://cumasu-1.firebaseio.com",
      "storageBucket": "cumasu-1.appspot.com",
      "serviceAccount": "cumasu.json"
    }

    #Database
    firebase = pyrebase.initialize_app(config)

    auth = firebase.auth()
    #authenticate a user
    user = auth.sign_in_with_email_and_password("nickscene1@gmail.com", "cumasu")

    db = firebase.database()

    # Get msg + phone number from Twilio
    message = request.values.get('Body', None)
    phone_number = request.values.get('From', None)

    # Save the message to the database
    data = {"message": message}
    db.child("users").child(phone_number).set(data, user['idToken'])

    # Add a message
    resp.message("What date should we set your appointment for?")
    return str(resp)
    
    

    #read response
 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

