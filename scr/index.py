from random import choice as randchoice
import requests
from pprint import pprint

def pullAPI():
    userData = requests.get("https://evanator05.github.io/SecretSantaServer/json/users.json")
    data = userData.json()
    pprint(data)

def getPairs(people):
    pairs = dict()
    for person in people:
        pair = randchoice(people)
        while pair == person:
            pair = randchoice(people)
        pairs[person] = pair

pullAPI()
