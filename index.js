

firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    // User is signed in.
    var email = user.email;
	firebase.database().ref('/users/' + user.uid +'/verifiedByAdmin').once('value').then(function(snapshot) {
	  if(snapshot.val())
	  {
		signin(email);
	  }
	  else{
		  alert("Oops!! you aren't a verified user.");
		  firebase.auth().signout();
	  }
	  // ...
	});
	
    // ...
  } else {
    // User is signed out.
	signout();
    // ...
  }
});


function Check_creds()
{
	const email=document.getElementById("userem").value;
	const pass=document.getElementById("userpw").value;
	const auth=firebase.auth();
	const promise=auth.signInWithEmailAndPassword(email, pass);
	promise.catch(e => efunc(e.code,e.message));
}