import requests


class APIClient:
    def fetch_json_data(self, url):
        response = requests.get(url)
        response.raise_for_status() 
        data = response.json()
        return data
