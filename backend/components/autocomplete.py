# Build trie to json
import json
from trie import Trie 

test_words = ['Foo', 'Fosh', 'Big', 'Bibble', 'Blasted']
autocompleter = Trie()



autocompleter.addlist(test_words)
with open('places.json', 'w') as f:
    json.dump(autocompleter.to_dict(), f)
# print(f'With prefix B {autocompleter.autocomplete("Bi")}')