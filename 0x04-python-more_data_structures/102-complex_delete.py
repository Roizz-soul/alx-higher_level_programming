#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for j in range(len(a_dictionary)):
        for i in a_dictionary:
            if a_dictionary[i] == value:
                del a_dictionary[i]
                break
    return a_dictionary
