import math
import os
# Constants
FILE_DIRECTORY = "src/textfiles"

# Utility functions


def add_padding(binary_code: str, header_size: int) -> tuple[int, str]:
    """Add padding to the given binary code if its length is not dividable by 8.

    Args:
        binary_code (str): The binary code to be padded.
        header_size (int): The length of the given code.

    Returns:
        tuple of (int, str): A tuple containing the length of the padding added 
                            and the padded code.
    """
    padding_length = (8 - header_size) % 8
    padded_code = "0" * padding_length + binary_code

    return padding_length, padded_code


def calculate_min_bits_needed(value):
    """Calculate the minimum number of bits needed to represent the given value.

    Args:
        value (int): The integer value for which the minimum number of bits needs to be calculated.

    Returns:
        bits_needed (int): The integer value of minimum bits needed to represent
                            the value.
    """
    bits_needed = math.ceil(math.log2(value + 1))
    return bits_needed


def list_non_empty_text_files():
    """Create a list of text files that can be compressed.

    This method will go through all the files from the directory with the extension ".txt"
    and adds the file to the list if its not empty.

    Returns:
         text_files (list): A list containing the file info for each file. Each list
                            element is a list with the format [number, filename, filesize].
    """
    text_files = []
    number = 0
    for filename in os.listdir(FILE_DIRECTORY):
        if filename.endswith(".txt"):
            file_path = os.path.join(FILE_DIRECTORY, filename)
            size = os.path.getsize(file_path) / 1024
            if size > 0:
                number += 1
                text_file = [number, filename, size]
                text_files.append(text_file)

    return text_files
