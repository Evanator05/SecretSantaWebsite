import requests

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
