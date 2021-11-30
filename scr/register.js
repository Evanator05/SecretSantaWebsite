var postURL = "http://50.99.113.163:25549/"
var pullURL = "http://50.99.113.163:25550/users.json"

function makeUser(username, password, firstName, lastName, bio) {
      var user = { //make user JSON object
          "username": username,
          "firstName": firstName,
          "lastName": lastName,
          "target":"Picked December First",
          "password": password,
          "bio": bio
          }

      return user
}


function getUserIndex(data, username) {
  for(let i = 0; i < data.users.length; i++) {
    if (data.users[i].username == username) {
      return i
    } else {
      return null
    }
  }
}

function setCookie(cName, cValue, expDays) {
        let date = new Date();
        date.setTime(date.getTime() + (expDays * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();
        document.cookie = cName + "=" + cValue + "; " + expires + "; path=/";
}


function registerAccount() {
  let username = document.getElementById("username").value
  let firstName = document.getElementById("firstName").value
  let lastName = document.getElementById("lastName").value
  let password = document.getElementById("password").value
  let confirmPassword = document.getElementById("confirmPassword").value
  let bio = document.getElementById("bio").value
  if (password == confirmPassword) {
    user = makeUser(username, password, firstName, lastName, bio)
    $.post(postURL, user);
    setCookie("username", username, 15)
    setCookie("password", password, 15)
    console.log(document.cookie)

  } else {
    returnError("Passwords do not match")
  }
}

function returnError(error) {
  document.getElementById("error").innerHTML = error
}
