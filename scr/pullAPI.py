import requests
from util import Util

class PullAPI:

    def __init__(self, url):
        self.data = requests.get(url)

    def pull():
        if self.data.status_code == 200:
            userData = self.data.json()
        else:
            print('Endpoint did not connect')
            return None
        return userData

requests.post("http://192.168.1.70:25549/", Util.makeUser("antwon", "123ABCa", "david", "michchelcee", "I love femboys"))
