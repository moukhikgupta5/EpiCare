// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyAckqRrDkeFhWCZ0kqS-_tE-8DzL0AHJ9E",
    authDomain: "seizure-detection-1f412.firebaseapp.com",
    databaseURL: "https://seizure-detection-1f412-default-rtdb.firebaseio.com",
    projectId: "seizure-detection-1f412",
    storageBucket: "seizure-detection-1f412.appspot.com",
    messagingSenderId: "589441294118",
    appId: "1:589441294118:web:e36c504db55586f8372be7"
  };
  
  // Initialize Firebase
firebase.initializeApp(firebaseConfig);

var pbTokkenEdit = document.getElementById("PushBulletTocken").innerText;

var pbTokken = pbTokkenEdit.replaceAll(".", "(*)");

var refLast = firebase.database().ref(`/${pbTokken}/`).limitToLast(1);


var locationData = ""; 


refLast.once("value")
  .then(function(snapshot) {
    snapshot.forEach(function(childSnapshot) {

      var key = childSnapshot.key;

      var childData = childSnapshot.val();
      locationData = childData.location;
      
  });
});