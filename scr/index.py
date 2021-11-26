from random import choice as randchoice
from pprint import pprint
import json, hashlib, requests

def pullAPI():
    data = requests.get("https://evanator05.github.io/SecretSantaServer/json/users.json").json()#get json from website
    return data
    pprint(len(data["users"]))

def getUserIndex(data, name):
    for i in range(len(data["users"])):
        if data["users"][i]["name"]["username"] == name:
            return i

def encryptString(hash_string):
    sha_signature = hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


with open('output.json', 'a') as out
