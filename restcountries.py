import pandas as pd
from columns import CountriesColumns
from api_client import APIClient

class RestCountries(CountriesColumns):
    
    def __init__(self, api_client: APIClient, base_url: str) -> None:
        self._all_countries_df: pd.DataFrame = None
        self.base_url = base_url
        self.api_client = api_client
        
    @property
    def all_countries_df(self) -> pd.DataFrame:
        if self._all_countries_df is None:
            self.get_all_countries()
        return self._all_countries_df
    
    @all_countries_df.setter
    def all_countries_df(self, df) -> None:
        self._all_countries_df = df
        
    def get_all_countries(self) -> None:
        url = '/all'
        response = self.__get_json(f'{self.base_url}{url}')
        data = self.__parse_json(response)
        self.all_countries_df = pd.DataFrame(data)
        
    def __parse_json(self, json) -> list:
        data = []
        for item in json:
            row = {
                self.COUNTRY_NAME: item.get('name', {'official':''}).get('official'),
                self.CAPITAL_NAME: item.get('capital', [''])[0],
                self.FLAG: item.get('flags', {'png':''}).get('png')
            }
            data.append(row)
        return data
        
    def __get_json(self, url) -> dict:
        return self.api_client.fetch_json_data(url)