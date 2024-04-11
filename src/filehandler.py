import os.path


class FileHandler():
    def __init__(self, path) -> None:
        self.path = path

    def get_new_path(self, extension):
        directory, filename = os.path.split(self.path)
        input_file_name = os.path.splitext(filename)[0] + extension
        new_path = directory + "/" + input_file_name
        return new_path

    def read_file(self):
        """Read a file and return its contents as a string.

        Returns:
            text (str): A string that contains the content of the file.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            text = file.read()

        return text

    def write_decoded_text_to_file(self, data):
        new_path = self.get_new_path("_decompressed.txt")

        with open(new_path, "w", encoding="utf-8") as file:
            file.write(data)

    def read_binary_file(self):
        """Read a binary file and return its content as a string representing binary data.

        Returns:
            str: The content of the binary file formatted as a string.
        """
        new_path = self.get_new_path(".bin")
        with open(new_path, "rb") as file:
            bytes_data = file.read()
            binary_string = "".join(format(byte, "08b") for byte in bytes_data)
        return binary_string

    def write_data_to_binary_file(self, data):
        """Write given data to binary file.

        Args:
            binary_header (bytearray): The content to be written.
        """
        new_path = self.get_new_path(".bin")
        with open(new_path, "wb") as file:
            file.write(data)
