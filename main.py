from api_client import APIClient
from restcountries import RestCountries
from ebay_scraping import EbayScraping

def main() -> None:
    print(f'restcountries: \n{rest_countries.all_countries_df}')
    print(f'Hat Cap: \n {hat_cap.data}')


if __name__ == "__main__":
    restcountries_link = 'https://restcountries.com/v3.1'
    ebay_link = 'https://www.ebay.com/itm/276458472230'
    try:
        
        api_client = APIClient()
        
        rest_countries = RestCountries(
            api_client=api_client, 
            base_url=restcountries_link
            )
        
        hat_cap = EbayScraping(
            api_client=api_client,
            url=ebay_link
            )
        
        main()
        
    except Exception as e:
        raise Exception(e)