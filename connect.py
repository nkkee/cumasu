from pyrebase import pyrebase
config = {
  "apiKey": "AIzaSyBg0TlfTsH8qjIU8VnmNJ8rTb8e5TK8b0c",
  "authDomain": "cumasu-1.firebaseapp.com",
  "databaseURL": "https://cumasu-1.firebaseio.com",
  "storageBucket": "cumasu-1.appspot.com",
  "serviceAccount": "cumasu.json"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
#authenticate a user
user = auth.sign_in_with_email_and_password("nickscene1@gmail.com", "cumasu")

db = firebase.database()

lana = {"message": "Message", "phone number": "12334354"}
db.child("agents").child("12345677").set(lana, user['idToken'])

lana_data = db.child("agents").child("12345677").child("phone number").get(user['idToken']).val()


print (lana_data)

