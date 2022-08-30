import json

# def write_data(city, attractions):
#     data.write("  {\n  ")
#     data.write(f"  \"basic-info\":")
#     data.write(f"{textwrap.indent(text=f'{response.text},', prefix='    ')}\n  ")
#     data.write(f"  \"advanced-info\":{textwrap.indent(text=detail_response.text, prefix='    ')}\n")
#     data.write("  },\n")

def parse_data(city):
    # read file
    with open(f'../data/{city}-Attraction-Data.json', 'r', encoding="utf8") as data_file:
        data = data_file.read()
    return json.loads(data)
