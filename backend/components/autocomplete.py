# Build trie to json
import json
import pandas as pd
from autocompleter import ReTrie 

test_words = ['Foo', 'Fosh', 'Big', 'Bibble', 'Blasted']
# df = pd.read_csv('autocomp_data.csv')
# cities = list(df['city_ascii'])

with open('places.json') as json_file:
    data = json.load(json_file)
    # print(data[1]['F'])

autocompleter = ReTrie(data=data)
# print(autocompleter.get_strings())
print(autocompleter.autocomplete("Muk"))
# print(f'With prefix Tok {autocompleter.autocomplete("Tok")}')