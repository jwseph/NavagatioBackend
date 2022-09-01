from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from .util import *

os.environ['PATH'] += r"C:\Development"
driver = webdriver.Chrome()


# TODO: Determine list of edge cases and add checks for them
def find_attractions(user_city_query, num_pages):
    """ Scrapes pages of attraction names for a certain city from trip advisor

    Parameters
    ----------
    user_city_query : str
        a string representing a city that the user wishes to search for. The code does not take in account of edge cases (whoops)

    num_pages : int
        an integer representing the number of pages a user wishes to scrape through. (Each page contains 0-30 attractions)
    """
    result = []
    num = 30
    url_string = f'https://www.tripadvisor.com/Search?q={user_city_query}&searchSessionId=E331623918D4BAD07396B370D0ADFA611661196804804ssid&searchNearby=false&sid=8F5B89C15E384480AF8856177B28B80D1661196805901&blockRedirect=true&rf=7&geo=1&ssrc=A'
    driver.get(url_string)
    driver.implicitly_wait(10)
    info = driver.find_element(By.XPATH, '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div/div/div')
    location_code = info.get_attribute('onclick').split(',')[9].split("'")[1]

    for index in range(1, num_pages+1):
        if index == 1:
            attraction_url = f'https://www.tripadvisor.com/Attractions-g{location_code}-Activities-a_allAttractions.true-{user_city_query}.html'
        else:
            attraction_url = f'https://www.tripadvisor.com/Attractions-g{location_code}-Activities-oa{30*index-1}-{user_city_query}.html'

        driver.get(attraction_url)
        attractions = driver.find_elements('xpath',
                                               '//*[@id="lithium-root"]/main/span/div/div[3]/div/div[2]/div[2]/span/div/div[3]/div/div[2]/div/div/section')

        for i in range(1, len(attractions)):
            attraction = attractions[i]

            if len(attraction.text) != 0:
                attraction_content = attraction.text.splitlines()
                surface_content = attraction_content[0: get_index(attraction_content, "By ")]

                if surface_content[0] == '2022':
                    surface_content.pop(0)

                try:
                    attraction_name = surface_content[0].split(".")[1].strip()
                except:
                    break

                result.append(attraction_name)

    driver.close()
    return result


def get_all_attraction_data(city, attractions):
    result = []
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

