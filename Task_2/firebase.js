const admin = require('firebase-admin');
var express = require('express');
var bodyParser = require('body-parser');
var app = express();

// Initialize Firebase
const serviceAccount = require('C:/Users/DiDa/Desktop/Task/pi-demo-5b792-firebase-adminsdk-t3d8v-669f4a9ef4.json');

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount)
});

const db = admin.firestore();
const collectionRef = db.collection('Task_2');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.post("/firebase", () => {

    const observer = collectionRef.onSnapshot(querySnapshot => {
        console.log('Received collection snapshot');
        querySnapshot.forEach(docSnapshot => {
          console.log(`Document ID: ${docSnapshot.id}`);
          console.log(docSnapshot.data());
        });
      }, err => {
        console.log(`Encountered error: ${err}`);
      });
});

app.post("/stop", () => {
  console.log("Stopping server...");
  // Perform any necessary cleanup or finalization tasks here
  process.exit(0); // Exit the process with a success status code
});

app.listen(3000);
// Listen for data changes on the entire collection



