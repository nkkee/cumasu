import os
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
 
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
        body="Finally it WORKED!")
    
    return '', 200

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)
 
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)