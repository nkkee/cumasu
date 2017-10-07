import os
from twilio.rest import Client


account_sid = os.environ["AC762f2156bfcaeff5a3e55d70d08ccc2f"]
auth_token = os.environ["8758a34c31ee3ec961dc6bd4724c54a2"]

client = Client(account_sid, auth_token)

client.messages.create(
	to="+13479053205",
	from_="+12012672115",
	body="This is the shit that made the Kessel Run"
)

