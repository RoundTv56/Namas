import requests

def get_country_info(country_name):
    base_url = "https://restcountries.com/v3.1/name/"
    url = f"{base_url}{country_name}"

    response = requests.get(url)

    if response.status_code == 200:
        country_data = response.json()[0]  # Assuming the first result is the desired country
        return {
            "name": country_data["name"]["common"],
            "population": country_data["population"],
            "currencies": country_data["currencies"],
            "languages": country_data["languages"],
        }
    else:
        return None
