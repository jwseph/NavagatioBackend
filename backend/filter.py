def user_pref(preferences=['Landmarks']):
    user_map = {}
    for preference in preferences:
        user_map[preference] = True


def filtering(data, user_map):
    count_matched = 0
    for attraction in data:
        attraction_types = attraction.candidates[0].types
        for _type in attraction_types:
            if user_map.get(_type) != None:
                count_matched += 1
    return count_matched

