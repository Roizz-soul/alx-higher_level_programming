#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = ""
    j = 0
    for i in str:
        if j == n:
            continue
        else:
            newStr[j] = i
        j++
    return newStr
