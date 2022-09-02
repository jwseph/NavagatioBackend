import json
import textwrap


def get_index(strings, substr):
    for idx, string in enumerate(strings):
        if substr in string:
            return idx
    return 3


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
