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
    count = 0
    with open(filename, mode="w", encoding="UTF-8") as file_n:
        file_n.write(text)
        for line in file_n:
            for char in line:
                count += 1
    return count
