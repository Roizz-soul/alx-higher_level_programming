#!/usr/bin/python3
""" text indentation function"""


def text_indentation(text):
    """prints text and replaces . ? : with a newline
    Args:
        text: text to be printed
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    b = 0
    for i in text:
        if b == 1 and i in " ":
            continue
        b = 0
        print(i, end="")
        if i in ".?:":
            b = 1
            print()
            print()
