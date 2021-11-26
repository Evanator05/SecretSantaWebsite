//Get Page Elements
var userName = document.getElementById("userName");
var firstName = document.getElementById("realName");
var bio = document.getElementById("bio");
var target = document.getElementById("target");

//Variables to populate
var uUserName = ""
var ufName = ""
var ulName = ""
var uBio = ""

var tFName = ""
var tLName = ""
var tUserName = ""

function pullData(accountName) {
  let userData

  var url = "https://evanator05.github.io/SecretSantaServer/json/users.json"
   userData = $.getJSON(url, function(data) {
      uUserName = data.users[0].name
   })
  console.log(uUserName)

}

function setHTML() {
  userName.innerHTML = uUserName;
  realName.innerHTML = ufName + " " + ulName;
  target.innerHTML = "Your target is: " + tFName + " " + tLName + " aka " + tUserName;
  bio.innerHTML = uBio;
}

function loadPage() {
  pullData();

};

loadPage();
