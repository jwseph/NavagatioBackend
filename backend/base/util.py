import requests
import json
import textwrap

import config as config


def get_index(strings, substr):
    for idx, string in enumerate(strings):
        if substr in string:
            return idx
    return 3


def get_place_data(city, attraction_name):
    url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={attraction_name}%20{city}&inputtype=textquery&fields=business_status%2Cformatted_address%2Cicon%2Cname%2Copening_hours%2Cphotos%2Cplace_id%2Cplus_code%2Cplace_id%2Cprice_level%2Crating%2Ctypes&key={config.api_key}"
    return requests.request("GET", url, headers={}, data={})


def get_place_detail_data(place_id):
    detail_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name%2Crating%2Cformatted_phone_number%2Cinternational_phone_number%2Creviews%2Curl%2Cvicinity%2Ctype%2Cutc_offset%2Cwebsite%2Copening_hours&key={config.api_key}"
    return requests.request("GET", detail_url, headers={}, data={})


def write_json_to(city, places_JSON_list, places_detail_JSON_list):
    data = open(f"{city}-Attraction-Data.json", "w", encoding="utf-8")
    data.write("[\n")
    for (place_json, place_detail_json) in zip(places_JSON_list, places_detail_JSON_list):
        data.write("  {\n  ")
        data.write(f"  \"basic-info\":")
        data.write(f"{textwrap.indent(text=f'{place_json},', prefix='    ')}\n  ")
        data.write(f"  \"advanced-info\":{textwrap.indent(text=place_detail_json, prefix='    ')}\n")
        data.write("  },\n")
    data.write("]")


def parse_data(city):
    # read file
    with open(f'../data/{city}-Attraction-Data.json', 'r', encoding="utf8") as data_file:
        data = data_file.read()
    return json.loads(data)