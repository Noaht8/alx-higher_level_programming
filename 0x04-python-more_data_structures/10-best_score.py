#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    sorted_list = sorted(a_dictionary.items(), key=lambda x: x[1], reverse=True)
    conv_list_to_dict = dict(sorted_list)
    biggest_value = list(conv_list_to_dict.values())[0]
    return biggest_value
