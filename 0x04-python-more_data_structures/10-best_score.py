#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) == 0:
        return None
    else:
        x = max(sorted(a_dictionary.values()))
        for i in a_dictionary:
            if a_dictionary[i] == x:
                return i
