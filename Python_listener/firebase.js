const admin = require('firebase-admin');

// Initialize Firebase
const serviceAccount = require('C:/Users/DiDa/Desktop/Task/pi-demo-5b792-firebase-adminsdk-t3d8v-669f4a9ef4.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

// Specify the document ID
const documentId = 'Boda'; // Replace with your desired document ID

// Add data to the specified document
const dataToAdd = {
  name: 'Abdullah',
  gender: 'Male',
  age:'22'
};

const docRef = db.collection('Test_2').doc(documentId);

docRef.set(dataToAdd)
  .then(() => {
    console.log(`Data added to document with ID: ${documentId}`);
  })
  .catch(error => {
    console.error(`Error adding data: ${error}`);
  });