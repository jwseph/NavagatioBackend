# Build trie to json
import json
from trie import Trie 

test_words = ['Foo', 'Fosh', 'Big', 'Bibble', 'Blasted']
autocompleter = Trie()

# with open('places.json', 'w') as f:
#     json.dump(autocompleter.to_dict(), f)

autocompleter.addlist(test_words)
print(f'With prefix B {autocompleter.autocomplete("Bi")}')