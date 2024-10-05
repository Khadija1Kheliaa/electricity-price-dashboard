"""
This file contains the function which fetches the electricity predictions for the next 24 hours.
"""
import requests


def fetch_data_for_next_24_hours():
    response = requests.get("https://api.awattar.at/v1/marketdata")
    return response.json()
