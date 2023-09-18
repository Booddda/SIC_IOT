import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import requests
import json
# Initialize Firebase
cred = credentials.Certificate("C:/Users/DiDa/Desktop/Task/pi-demo-5b792-firebase-adminsdk-t3d8v-669f4a9ef4.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Add Data
def add_data():
    doc_ref = db.collection('Task_2').document('Abdullah')
    data = {
        'name': 'Abdullah',
        'age':'22',
        'gender':'Male'
    }
    doc_ref.set(data)
    print("Data added.")
    return data

def initiate_post():
    res = requests.post('http://127.0.0.1:3000/firebase', json=add_data()) 
    return res.json()

def stop_server():
    res = requests.post('http://127.0.0.1:3000/stop')
    if res.status_code == 200:
        print("Server stopped successfully.")
    else:
        print("Failed to stop the server.")


if __name__ == '__main__':
    add_data()
    initiate_post()
    stop_server()