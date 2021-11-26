from random import choice as randchoice
from pprint import pprint
import json, hashlib, requests

def pullAPI():
    data = requests.get("https://evanator05.github.io/SecretSantaServer/json/users.json")
    if data.status_code == 200:
        userData = data.json()
    else:
        print('Endpoint did not connect')
        return None
    return userData

def getUserIndex(data, username):
    for i in range(len(data["users"])):
        if data["users"][i]["name"]["username"] == username:
            return i
    else:
        return None

def encryptString(hash_string):#encrypt a string
    return hashlib.sha256(hash_string.encode()).hexdigest()

def makeUser(username, password, firstName, lastName, bio):
    user = { #make user JSON object
        "name": {
            "username": username,
            "firstName": firstName,
            "lastName": lastName
        },
        "target":"Picked December First",
        "password": encryptString(password), #password encrypted with sha256 making it uncrackable
        "bio": bio
    }
    return user

json_object = json.dumps(generateUsers())#make the dict a json file
print(json_object)

data = requests.post("https://evanator05.github.io/SecretSantaServer/json/users.json", json_object)
