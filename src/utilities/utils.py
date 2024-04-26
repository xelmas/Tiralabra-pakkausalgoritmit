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
