from random import choice as randchoice
import json, hashlib

class Util():

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
