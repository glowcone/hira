// Initialitze Firebase
const config = {
	apiKey: "AIzaSyDmqf-q8xMecvvZUykuP8OadFGhYkmTOps",
	authDomain: "la-hacks-2018-1522510422362.firebaseapp.com",
	databaseURL: "https://la-hacks-2018-1522510422362.firebaseio.com",
	projectId: "la-hacks-2018-1522510422362",
}

firebase.initializeApp(config);
const database = firebase.database();

function writeData(title, transcript) {
	console.log(title)
	console.log(transcript)
  database.ref().child('notes').push({
		title: title,
		transcript: transcript
  });
}

function readData() {
	return database.ref('notes').once('value');
}
