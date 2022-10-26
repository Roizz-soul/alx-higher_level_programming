#!/usr/bin/python3
"""Append file function"""


def append_write(filename="", text=""):
    """opens and appends a file
    Args:
        filename: name of the file
        text: string to be written into file
    Returns:
        the number of characters added
    """
    with open(filename, mode="a", encoding="UTF-8") as file_n:
        return file_n.write(text)
