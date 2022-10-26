#!/usr/bin/python3
"""Write file function"""


def write_file(filename="", text=""):
    """opens and writes into a file
    Args:
        filename: name of the file
        text: string to be written into file
    Returns:
        the number of characters written
    """
    with open(filename, mode="w", encoding="UTF-8") as file_n:
        return file_n.write(text)
