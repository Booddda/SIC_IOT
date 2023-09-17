import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Initialize Firebase
cred = credentials.Certificate("C:/Users/DiDa/Desktop/Task/pi-demo-5b792-firebase-adminsdk-t3d8v-669f4a9ef4.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Add Data
def add_data():
    doc_ref = db.collection('Test1').document('Omar')
    doc_ref.set({
        'name': 'Boda',
        'age':'22',
        'gender':'Male'

    })
    print("Data added.")



if __name__ == '__main__':
    add_data()