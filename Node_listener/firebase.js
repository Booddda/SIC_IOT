const admin = require('firebase-admin');

// Initialize Firebase
const serviceAccount = require('C:/Users/DiDa/Desktop/Task/pi-demo-5b792-firebase-adminsdk-t3d8v-669f4a9ef4.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();

// Listen for data changes on the entire collection
const collectionRef = db.collection('Test1');

const observer = collectionRef.onSnapshot(querySnapshot => {
  console.log('Received collection snapshot');
  querySnapshot.forEach(docSnapshot => {
    console.log(`Document ID: ${docSnapshot.id}`);
    console.log(docSnapshot.data());
  });
}, err => {
  console.log(`Encountered error: ${err}`);
});

