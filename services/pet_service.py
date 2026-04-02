import random
import json
from utils.api_client import APIClient
from pathlib import Path

class PetService:
    def __init__(self):
        self.api = APIClient()
        self.payload_template = json.loads(Path("data/create_pet.json").read_text())

    def random_category(self):
        base = ["Electronics", "Books", "Fashion", "Sports", "Pets"]
        return f"{random.choice(base)}-{random.randint(100,999)}"

    def create_pet(self):
        id = random.randint(1000,9999)
        category_id = random.randint(1000,9999)
        payload = self.payload_template.copy()
        payload["id"] = id
        payload["category"] = {
            "id": category_id,
            "name": self.random_category()
        }

        response = self.api.post("/v2/pet", json=payload)

        return response.json()