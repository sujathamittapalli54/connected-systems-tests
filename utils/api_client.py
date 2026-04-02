import requests
from utils.config import API_URL

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.base_url = API_URL

    def get(self, endpoint):
        return self.session.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint, json=None):
        return self.session.post(f"{self.base_url}{endpoint}", json=json)