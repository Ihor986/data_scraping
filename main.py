from api_client import APIClient
from restcountries import RestCountries

def main():
    print(rest_countries.all_countries_df)


if __name__ == "__main__":
    api_client = APIClient()
    rest_countries = RestCountries(
        api_client=api_client, 
        base_url='https://restcountries.com/v3.1'
        )
    
    main()