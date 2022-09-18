import json
def user_pref(preferences=['tourist_attraction', 'park']):
    user_prefs = {}
    for preference in preferences:
        user_prefs[preference] = True
    return user_prefs


def filtering(data, user_prefs):
    matched_tags = {}
    for attraction in data:
        attraction_types = attraction['basic_info']['candidates'][0]['types']
        for _type in attraction_types:
            if user_prefs.get(_type) != None:
                if matched_tags.get(attraction['basic_info']['candidates'][0]['name']) != None:
                   matched_tags[attraction['basic_info']['candidates'][0]['name']]+=1
                else:
                    matched_tags[attraction['basic_info']['candidates'][0]['name']] = 1 

    return sorted(matched_tags.items(), key=lambda x: x[1], reverse=True)
    
dicts = json.loads(open(r'data\Seoul-Attraction-Data.json', 'rb').read().decode('utf-8'))
print(filtering(dicts, user_pref()))