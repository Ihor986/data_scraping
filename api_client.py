import requests


class APIClient:
    
    def fetch_data(self, url) -> requests.Response:
        response = requests.get(url)
        response.raise_for_status() 
        return response
    
