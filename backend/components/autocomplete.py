# Build trie to json
import json
import pandas as pd
from trie import Trie 

test_words = ['Foo', 'Fosh', 'Big', 'Bibble', 'Blasted']
df = pd.read_csv('autocomp_data.csv')
cities = list(df['city_ascii'])
# with open('places.json') as json_file:
#     data = json.load(json_file)
#     print(data[1])

autocompleter = Trie()

autocompleter.addlist(cities)
with open('places.json', 'w') as f:
    json.dump(autocompleter.to_dict(), f)
print(f'With prefix B {autocompleter.autocomplete("Tok")}')