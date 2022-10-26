#!/usr/bin/python3
"""Read file function"""


def read_file(filename=""):
    """opens and prints the contents of a file"""
    with open(filename, encoding='UTF-8') as file_n:
        print(file_n.read())
