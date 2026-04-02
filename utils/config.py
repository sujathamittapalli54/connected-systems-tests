import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_URL = os.getenv("API_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")