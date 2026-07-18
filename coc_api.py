import os
import requests

BASE_URL = "https://api.clashofclans.com/v1"

API_TOKEN = os.getenv("COC_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "application/json"
}


def get_player(tag):
    if not API_TOKEN:
        print("❌ COC_API_TOKEN environment variable is not set.")
        return None

    tag = tag.strip().upper()

    if tag.startswith("#"):
        tag = tag[1:]

    url = f"{BASE_URL}/players/%23{tag}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=15)

        print(f"🌐 Request: {url}")
        print(f"📡 Status: {response.status_code}")

        if response.status_code == 200:
            return response.json()

        print("❌ API Error:")
        print(response.text)
        return None

    except Exception as e:
        print(f"❌ Request failed: {e}")
        return None
