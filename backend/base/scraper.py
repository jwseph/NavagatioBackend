from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from util import *

os.environ['PATH'] += r"C:\Development"
driver = webdriver.Chrome()


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

        print(attraction_url)
        driver.get(attraction_url)
        attractions = driver.find_elements('xpath',
                                               '//*[@id="lithium-root"]/main/span/div/div[3]/div/div[2]/div[2]/span/div/div[3]/div/div[2]/div/div/section')
        for i in range(1, len(attractions)-1):
            # rating_array = []
            attraction = attractions[i]

            if len(attraction.text) != 0:
                attraction_content = attraction.text.splitlines()
                surface_content = attraction_content[0: get_index(attraction_content, "By ")]

                if surface_content[0] == '2022':
                    surface_content.pop(0)

                attraction_name = surface_content[0].split(".")[1].strip()
                # TODO: Throw a check to see if the attraction exists or doenst, if no break, otherwise continue?
                print(attraction_name)
    driver.close()


find_attractions("Mukilteo", 1)