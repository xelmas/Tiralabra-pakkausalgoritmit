import os.path


class FileHandler():
    """Class that handles reading and writing the files.

    Attributes: 
        path (str): The path to file to be compressed/decompressed.
        file_size (bytes): The size of the file in bytes.
    """

    def __init__(self, path) -> None:
        """Create a new instance of FileHandler.

        Args:
            path (str): The path to file.
        """
        self.path = path
        self.file_size = os.path.getsize(self.path)

    def generate_new_path(self, extension):
        """Generate a new file path with the given extension.

        Args:
            extension (str): The desired extension for the file.

        Returns:
            new_path (str): A new file path with the given extension.
        """
        directory, filename = os.path.split(self.path)
        input_file_name = os.path.splitext(filename)[0] + extension
        new_path = directory + "/" + input_file_name
        return new_path

    def get_file_size(self):
        return self.file_size

    def set_file_size(self, new_size: bytes):
        self.file_size = new_size

    def read_file(self):
        """Read a file and return its contents as a string.

        Returns:
            text (str): A string that contains the content of the file.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            text = file.read()

        return text

    def write_decoded_text_to_file(self, data):
        """Write the decoded text into a new file.

        This method creates a new text file with the same filename as the compressed binary file,
        but with the extension changed to "_decompressed.txt", for example
        "filename_decompressed.txt". If said file already exists, it will be overwritten.
        The size of the new file will be stored into the attribute file_size.

        Args:
            data (str): The decoded text to be written into the file.
        """
        new_path = self.generate_new_path("_decompressed.txt")

        with open(new_path, "w", encoding="utf-8") as file:
            file.write(data)

        self.set_file_size(os.path.getsize(new_path))

    def read_binary_file(self):
        """Read a binary file and return its content as a string representing binary data.

        Returns:
            str: The content of the binary file formatted as a string.
        """
        new_path = self.generate_new_path(".bin")
        with open(new_path, "rb") as file:
            bytes_data = file.read()
            binary_string = "".join(format(byte, "08b") for byte in bytes_data)
 
        return binary_string

    def write_data_to_binary_file(self, data: bytearray):
        """Write given data to binary file.

        This method will write the data into the binary file and the size of the new file will be
        stored into the attribute file_size.

        Args:
            binary_header (bytearray): The content to be written.
        """
        new_path = self.generate_new_path(".bin")
        with open(new_path, "wb") as file:
            file.write(data)

        self.set_file_size(os.path.getsize(new_path))
