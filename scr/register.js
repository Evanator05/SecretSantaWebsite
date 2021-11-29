var postURL = "http://192.168.1.70:25549/"
const Http = new XMLHttpRequest();


function makeUser(username, password, firstName, lastName, bio) {

      var user = { //make user JSON object
          "username": username,
          "firstName": firstName,
          "lastName": lastName,
          "target":"Picked December First",
          "password": password,
          "bio": bio
          }

      function hash(string) {
        const utf8 = new TextEncoder().encode(string);
        return crypto.subtle.digest('SHA-256', utf8).then((hashBuffer) => {
          const hashArray = Array.from(new Uint8Array(hashBuffer));
          const hashHex = hashArray
            .map((bytes) => bytes.toString(16).padStart(2, '0'))
            .join('');
          return hashHex;
        });
      }

      function makeObject(password) {
        user.password = password
      }

      hash(password).then(value => makeObject(value))
      console.log(user)
      return user
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
  }
}
