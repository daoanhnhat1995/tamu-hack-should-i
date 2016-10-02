from firebase import firebase

FIREBASE_URL = "https://tamuhack-should-i.firebaseio.com"
fb = firebase.FirebaseApplication(FIREBASE_URL, None)
response = fb.get('/results/',None);
print(response)


