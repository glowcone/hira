// Initialitze Firebase
const config = {
	apiKey: "AIzaSyDmqf-q8xMecvvZUykuP8OadFGhYkmTOps",
	authDomain: "la-hacks-2018-1522510422362.firebaseapp.com",
	databaseURL: "https://la-hacks-2018-1522510422362.firebaseio.com",
	projectId: "la-hacks-2018-1522510422362",
}

firebase.initializeApp(config);
const database = firebase.database();

var postKey = firebase.database().ref().child('notes').push().key;

function writeData(title, transcript) {
	console.log(title)
	console.log(transcript)
	console.log(postKey)
	var postData = {title: title, transcript: transcript};
	var updates = {};
	updates['/notes/' + postKey] = postData;
	return firebase.database().ref().update(updates)
  // database.ref().child('notes').update({
	// 	title: title,
	// 	transcript: transcript
  // });
}
