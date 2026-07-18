import os
import requests

API_TOKEN = os.getenv("COC_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}


def get_player(player_tag):
    player_tag = player_tag.replace("#", "%23")

    url = f"https://api.clashofclans.com/v1/players/{player_tag}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()

    return None
