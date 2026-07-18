import os
import requests

BASE_URL = "https://api.clashofclans.com/v1"

API_TOKEN = os.getenv("COC_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json"
}


def get_player(tag):
    tag = tag.replace("#", "%23")

    response = requests.get(
        f"{BASE_URL}/players/{tag}",
        headers=HEADERS
    )

    if response.status_code == 200:
        return response.json()

    return None
