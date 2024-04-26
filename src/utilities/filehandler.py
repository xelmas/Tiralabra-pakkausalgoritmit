import os.path
from utilities.utils import FILE_DIRECTORY


class FileHandler():
    """Class that handles reading and writing the files.

    Attributes:
        filename (str): The name of the file to be compressed/decompressed. 
        path (str): The path to file to be compressed/decompressed.
        file_size (bytes): The size of the file in bytes.
    """

    def __init__(self, filename) -> None:
        """Create a new instance of FileHandler.

        Args:
            filename (str): The name of the file.
        """
        self.filename = filename
        self.path = os.path.join(FILE_DIRECTORY, filename)
        self.file_size = os.path.getsize(self.path)

    def generate_new_path(self, extension):
        """Generate a new file path with the given extension.

        Args:
            extension (str): The desired extension for the file.

        Returns:
            new_path (str): A new file path with the given extension.
        """
        new_file_name = self.filename.split(".")[0] + extension
        new_path = FILE_DIRECTORY + "/" + new_file_name

        return new_path

    def get_file_size(self) -> bytes:
        """Get size of the given file.

        Returns:
            file_size (bytes): A size of the file in bytes.
        """
        return self.file_size

    def set_file_size(self, new_size: bytes):
        """Set size of the file.

        Args:
            new_size (bytes): A new size of the file.
        """
        self.file_size = new_size

    def read_file(self) -> str:
        """Read a file and return its contents as a string.

        Returns:
            text (str): A string that contains the content of the file.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            text = file.read()

        return text

    def find_extra_supported_symbols(self) -> list:
        """Find all the symbols that are outside the range of 0-255 unicode points and are present
        in the text.

        This method is used before compressing with the LZW algorithm, so that the dictionary of
        characters is initialized properly.

        Returns:
           extra_supported_symbols (list): A list containing all the symbols outside the range of
                                        0-255 unicode points that are found in the text.
        """
        text = self.read_file()
        extra_supported_symbols = []
        for char in text:
            unicode = ord(char)
            if unicode > 255 and char not in extra_supported_symbols:
                extra_supported_symbols.append(char)

        return extra_supported_symbols

    def remove_file(self, path):
        """Remove given file.

        Args:
            path (str): A path to the file to be removed.
        """
        os.remove(path)

    def tear_down(self):
        """Remove all the constructed files.

        This method removes all the files that were constructed during the decompression process
        """
        files = [file for file in os.listdir(
            FILE_DIRECTORY) if file.endswith("_decompressed.txt")]
        for file in files:
            os.remove(os.path.join(FILE_DIRECTORY, file))

    def write_decoded_text_to_file(self, data: str, algorithm_name: str):
        """Write the decoded text into a new file.

        This method creates a new text file with the same filename as the compressed binary file,
        but with the extension changed to "_decompressed.txt", for example
        "filename_Huffman_decompressed.txt". If said file already exists, it will be overwritten.
        The size of the new file will be stored into the attribute file_size.

        Args:
            data (str): The decoded text to be written into the file.
        """
        new_path = self.generate_new_path(
            f"_{algorithm_name}_decompressed.txt")

        with open(new_path, "w", encoding="utf-8") as file:
            file.write(data)

        self.set_file_size(os.path.getsize(new_path))

    def read_binary_file(self, algorithm_name: str) -> str:
        """Read a binary file and return its content as a string of binary data.

        This method reads the content of the binary file, formats each byte to an 8-bit
        representation, and concatenates them into a one string. The binary file is then removed.

        Returns:
            binary_data: The content of the binary file formatted as a string.
        """
        new_path = self.generate_new_path(f"_{algorithm_name}.bin")
        with open(new_path, "rb") as file:
            bytes_data = file.read()
            binary_data = "".join(format(byte, "08b") for byte in bytes_data)

        self.remove_file(new_path)
        return binary_data

    def write_data_to_binary_file(self, data: bytearray, algorithm_name: str):
        """Write given data to binary file.

        This method creates a new binary file with the same filename as original text file,
        but with the extension changed to "_algorithmName.bin", for example
        "filename_Huffman.bin". If said file already exists, it will be overwritten.
        The size of the new file will be stored into the attribute file_size.

        Args:
            data (bytearray): The content to be written.
        """
        new_path = self.generate_new_path(f"_{algorithm_name}.bin")
        with open(new_path, "wb") as file:
            file.write(data)

        self.set_file_size(os.path.getsize(new_path))
