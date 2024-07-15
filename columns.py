from abc import ABC

class CountriesColumns(ABC):
    COUNTRY_NAME = 'назва країни'
    CAPITAL_NAME = 'назва столиці'
    FLAG = 'прапор'
    
class EbayColumns(ABC):
    NAME = 'name'
    IMG = 'img'
    LINK = 'link'
    PRICE = 'price'
    SELLER = 'seller'
    DELIVERY_PRICE = 'delivery_price'
    