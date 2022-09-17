import json
import pandas as pd
import os
class Autocompleter:
    def __init__(self, data):
        self.data = data
        self.autocomplete_data = pd.read_csv('backend/library/autocomp_data.csv')

    def get_strings(self, node1):
        def get(node, string, strings):
            if node[0]:
                strings.append("".join(string))
            for char in node[1]:
                string.append(char)
                get(node[1][char], string, strings)
                string.pop()
        strings = []
        get(node1, [], strings)
        return strings

    # Autocomplete Functions
    def autocomplete(self, prefix):
        # def process(result, df):
        #     processed_data = []
        #     for city in result:
        #         point = {}
        #         point['city'] = city
        #         point['country'] = df['city' == city]['country'] if df['city' == city]['country'] != None else 'null'
        #         processed_data.append(point)

        #     return processed_data

        node = self.data
        for char in prefix:
            if char not in node[1]:
                return []
            node = node[1][char]

        results = [prefix + string for string in self.get_strings(node)]
        
        if len(results) > 20:
            return results[:25]
        return results

def autocomp_init(path='places.json'):
    with open(path) as json_file:
        data = json.load(json_file)
    return Autocompleter(data=data)

