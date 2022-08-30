import json
import textwrap
import backend.config as config

import requests
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"C:\Development"
driver = webdriver.Chrome()


def get_index(strings, substr):
    for idx, string in enumerate(strings):
        if substr in string:
            return idx
    return 3


# user_city_query = "Beijing"
# num_pages = 3


def find_attractions(user_city_query, num_pages):
    url_string = f'https://www.tripadvisor.com/Search?q={user_city_query}&searchSessionId=E331623918D4BAD07396B370D0ADFA611661196804804ssid&searchNearby=false&sid=8F5B89C15E384480AF8856177B28B80D1661196805901&blockRedirect=true&rf=7&geo=1&ssrc=A'
    driver.get(url_string)
    driver.implicitly_wait(10)
    info = driver.find_element(By.XPATH, '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div')
    location_code = info.get_attribute('onclick').split(',')[9].split("'")[1]

    # data = open(f"{city}-Attraction-Data.json", "w", encoding="utf-8")
    # data.write("[\n")

    for index in range(1, num_pages+1):
        print(index)
        if index == 1:
            attraction_url = f'https://www.tripadvisor.com/Attractions-g{location_code}-Activities-a_allAttractions.true-{user_city_query}.html'
        else:
            attraction_url = f'https://www.tripadvisor.com/Attractions-g{location_code}-Activities-oa{30*index-1}-{user_city_query}.html'

            # print(attraction_url)
            # get_page_content(attraction_url)
        print(attraction_url)
        driver.get(attraction_url)
        attractions = driver.find_elements('xpath',
                                               '//*[@id="lithium-root"]/main/span/div/div[3]/div/div[2]/div[2]/span/div/div[3]/div/div[2]/div/div/section')
        for i in range(1, 39):
            # rating_array = []
            attraction = attractions[i]

            if len(attraction.text) != 0:
                attraction_content = attraction.text.splitlines()
                surface_content = attraction_content[0: get_index(attraction_content, "By ")]

                if surface_content[0] == '2022':
                    surface_content.pop(0)

                attraction_name = surface_content[0].split(".")[1].strip()

                # try:
                #     type_of = surface_content[2].split(' • ')
                # except:
                #     type_of = 'N/A'

                # try:
                #     if 'admission' in surface_content[3]:
                #         admission = surface_content[3]
                #         location = user_city_query
                #     else:
                #         admission = 'Cost Varies'
                #         location = surface_content[3]

                # except:
                #     location = 'N/A'

                # print(f'{i}  Attraction: ({attraction_name}) Type: {type_of} Cost: ({admission}) Location:({location})')
                #
                url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input={attraction_name}%20{user_city_query}&inputtype=textquery&fields=business_status%2Cformatted_address%2Cicon%2Cname%2Copening_hours%2Cphotos%2Cplace_id%2Cplus_code%2Cplace_id%2Cprice_level%2Crating%2Ctypes&key={config.api_key}"
                payload = {}
                headers = {}

                response = requests.request("GET", url, headers=headers, data=payload)
                print(response.text)
                place_id = response.json().get("candidates")[0].get('place_id')

                detail_url = f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name%2Crating%2Cformatted_phone_number%2Cinternational_phone_number%2Creviews%2Curl%2Cvicinity%2Ctype%2Cutc_offset%2Cwebsite%2Copening_hours&key={config.api_key}"
                detail_response = requests.request("GET", detail_url, headers=headers, data=payload)
                print(detail_response.text)
    # data.write("]")
    driver.close()


find_attractions("Mukilteo", 1)