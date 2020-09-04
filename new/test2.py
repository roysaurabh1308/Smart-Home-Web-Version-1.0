import pyrebase
import datetime

config={
    "apiKey": "AIzaSyBcXcAtVqPT87iAxDgi9ilV5XhIkMIcdv0",
    "authDomain": "smart-home-1343e.firebaseapp.com",
    "databaseURL": "https://smart-home-1343e.firebaseio.com",
    "projectId": "smart-home-1343e",
    "storageBucket": "smart-home-1343e.appspot.com",
    "messagingSenderId": "228104491397",
    "appId": "1:228104491397:web:3b561ae413e0aa9bf7b4ec",
    "measurementId": "G-NBBEN0BRWF"

}

firebase = pyrebase.initialize_app(config)
db=firebase.database()
stg=firebase.storage()
x = datetime.datetime.now()
l=0
temp=db.child("intruders").shallow().get().val()
if temp:
    l=len(temp)
ipath="intruders/intruder"+str(l)+".jpg"
stg.child(ipath).put("intruder0.jpg")
url=stg.child(ipath).get_url(None)
data=x.isoformat().replace('.',':')
db.child("intruders/"+data).set(str(url))