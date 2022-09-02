import requests
from . import scraper
from .config import api_key


# GOOGLE PLACES API ACCESS
def get_place_data(city, attraction_name):
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={attraction_name}%20{city}&inputtype=textquery&fields=business_status%2Cformatted_address%2Cicon%2Cname%2Copening_hours%2Cphotos%2Cplace_id%2Cplus_code%2Cplace_id%2Cprice_level%2Crating%2Ctypes&key={api_key}"
    return requests.request("GET", url, headers={}, data={})


def get_place_detail_data(place_id):
    detail_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name%2Crating%2Cformatted_phone_number%2Cinternational_phone_number%2Creviews%2Curl%2Cvicinity%2Ctype%2Cutc_offset%2Cwebsite%2Copening_hours&key={api_key}"
    return requests.request("GET", detail_url, headers={}, data={})


def get_all_attraction_data(city):
    result = []
    attractions = scraper.find_attractions(city)
    for attraction in attractions:
        place_data = get_place_data(city, attraction)
        # TODO: Some error here (Place id doesnt exist?)
        """
            place_id = place_data.json().get("candidates")[0].get('place_id')
        """
        place_id = place_data.json().get("candidates")[0].get('place_id')

        place_detail_data = get_place_detail_data(place_id)

        result.append({'basic-info': place_data.json(), 'advanced-info': place_detail_data.json()})

    return result
