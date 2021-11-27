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

requests.post("http://127.0.0.1:5000/", Util.makeUser("area51rocks", "cumnuts", "arend", "rea", "my name is arend and I love anime and balls"))
