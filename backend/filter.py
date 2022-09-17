import json
def user_pref(preferences=['Landmarks']):
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
                matched_tags[attraction['basic_info']['candidates'][0]['name']] += 1

    return sorted(matched_tags.items(), key=lambda x: x[1])
    
dicts = json.loads(open(r'backend\Mukilteo-Attraction-Data.json', 'rb').read().decode('utf-8'))
print(filtering(dicts, user_pref()))