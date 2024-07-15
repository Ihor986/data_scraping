import json
from columns import EbayColumns
from api_client import APIClient
from bs4 import BeautifulSoup


class EbayScraping(EbayColumns):
    
    def __init__(self, api_client: APIClient, url: str) -> None:
        self.api_client: APIClient = api_client
        self._data: dict = None
        self._url: str = url
        
    @property
    def data(self) -> str:
        if self._data is None:
            self.update_data()
        return json.dumps(self._data, indent=4)
    
    @data.setter
    def data(self, value: dict) -> None:
       self._data = value 
        
    def update_data(self, url: str = None) -> None:
        if url is not None:
            self._url = url
        response = self.api_client.fetch_data(self._url)
        soup = BeautifulSoup(response.content, 'html.parser')
        result_dict = {
        self.NAME: soup.find(attrs={'class' : 'x-item-title__mainTitle'}).text,
        self.IMG: soup.find(attrs={'class' : 'ux-image-carousel-item'}).find('img').attrs.get('src'),
        self.LINK: self._url,
        self.PRICE: soup.find(attrs={'class' : 'x-price-primary'}).text,
        self.SELLER: soup.find(attrs={'class' : 'x-sellercard-atf__info__about-seller'}).attrs.get('title'),
        self.DELIVERY_PRICE: ([item.find(attrs={'class': 'ux-labels-values__values-content'}).find('span').text
                               for item in soup.find_all(attrs={'data-testid' : 'ux-labels-values'})
                               if item.find(attrs={'class' : 'ux-textspans'}).text == 'Shipping:'])[0]
        }
        self.data = result_dict
        