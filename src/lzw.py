
class LZW():
    """Class for Lempel-Ziv-Welch algorithm.

    Implements the LZW-algorithm for text compression and decompression.

    Attributes: 
        table (dict): The dictionary for characters and their corresponding code values.
        filehandler (FileHandler): The FileHandler object provided during initialization.
    """

    def __init__(self, filehandler) -> None:
        """Create a new instance of LZW-algorithm.

        Args:
            filehandler (FileHanlder): An instance of the FileHandler class.
        """
        self.table = None
        self.filehandler = filehandler

    def _init_table(self, compress=True):
        """Initialize the dictionary for characters and their corresponding code values.

        Method initializes the table based on the boolean value given:
        - If the value is true, table is initialized for compression, and then the keys are 
        characters and values are their codes in the dictionary.
        - If the value is False, table is initialized for decompression, and then the keys are
        codes and values are their corresponding characters.

        Constructed dictionary is stored in the variable self.table.

        Args:
            compress (bool, optional): The value to determine which method is going to be used.
                                    If True, initialize table for compression, otherwise
                                    initialize for decompression. Defaults to True.
        """
        table = {}
        for i in range(0, 256):
            char = ""
            char += chr(i)
            if compress:
                table[char] = i
            else:
                table[i] = char
        self.table = table

    def get_table(self):
        """Return the initialized dictionary for characters and their corresponding code values.

        Returns:
            table (dict): The dictionary for mapping characters and their code values.
        """
        return self.table

    def encode(self, text_stream):
        """Encode the given text from the file.

        This method processes the text stream and updates the dictionary that keeps track of the
        characters/sequences and their codes. When the encoding starts, there are all possible
        single characters in the table mapped with their code values 0-255. As the text stream is
        processed, new sequences are added to the table and the code value is raised by one.
        The list containing encoded text is constructed at the same time, adding the code value for
        character/sequence to it.

        Args:
            text_stream (str): The text in ASCII format to be encoded.

        Returns:
            encoded_text (list): The encoded text as a list, where characters/sequences are 
                                replaced with their code values.
        """
        first_char = text_stream[0]
        index = 0
        code = 256
        encoded_text = []

        while index < len(text_stream):
            if index != len(text_stream)-1:
                next_char = text_stream[index+1]
            else:
                next_char = ""

            if first_char + next_char in self.table:
                first_char += next_char
            else:
                encoded_text.append(self.table[first_char])
                self.table[first_char + next_char] = code
                code += 1
                first_char = next_char
            index += 1
        encoded_text.append(self.table[first_char])
        return encoded_text

    def _add_padding(self, code, header_size):
        """Add padding to the given code if its length is not dividable by 8.

        Args:
            code (str): The code to be padded.
            header_size (int): The length of the given code.

        Returns:
            tuple of (int, str): A tuple containing the length of the padding added 
                                and the padded code.
        """
        padding_length = (8 - header_size) % 8
        padded_code = "0" * padding_length + code
        return padding_length, padded_code

    def create_header(self, data):
        """Create a complete header data with a string representation of binary data.

        The data is formatted with the following logic:
            - The length of the padding of data (8 bits).
            - The padded data.

        Args:
            data (str): The text to encode and create a header for.

        Returns:
            complete data (str): The complete data represented as a string of binary data.
        """
        binary_string = "".join(format(number, "012b") for number in data)
        length_data = len(binary_string)
        len_header = length_data + 8
        padding_len, padded_data = self._add_padding(binary_string, len_header)
        padding_len_bin = format(padding_len, "08b")

        data_array = []
        data_array.append(padding_len_bin)
        data_array.append(padded_data)
        complete_data = "".join(data for data in data_array)
        return complete_data

    def convert_data_to_bytes(self, header):
        """Convert a string of header data to bytes.

        Args:
            header_data (str): The string of header data to be converted.

        Returns:
            encoded_bytes (bytearray): The converted data as an array of bytes.
        """
        encoded_bytes = bytearray()
        for i in range(0, len(header), 8):
            byte = header[i:i+8]
            byte_value = int(byte, 2)
            encoded_bytes.append(byte_value)
        return encoded_bytes

    def compress(self, text):
        """Compress the text using LZW-algorithm.

        This method initializes the table, encodes the text and generates a bytearray header that
        represents the compressed data.

        Args:
            text (str): The text to be compressed.

        Returns:
            compressed_header_in_binary (bytearray): The header data represented as a bytearray.
        """

        self._init_table(compress=True)
        encoded_text_array = self.encode(text)
        header_str = self.create_header(encoded_text_array)
        compressed_header_in_binary = self.convert_data_to_bytes(header_str)
        return compressed_header_in_binary

    def compress_file(self):
        """Compress the file given during initialization.

        This method compresses the file given in the constructor. It reads the content of the file,
        compresses the text and calls filehandler-object to write the text in bytearray format
        into the file.
        """
        text = self.filehandler.read_file()
        header_in_binary = self.compress(text)
        self.filehandler.write_data_to_binary_file(header_in_binary)

    def decode_text(self, compressed_code):
        """Decode the compressed codes to text.

        When the decoding starts, there are all possible single characters in the table mapped
        with their code values 0-255. While decoding is processed, the table is updated for each
        character (except the first). The text is decoded by reading the compressed codes and
        replacing them with their corresponding characters/sequences.

        Args:
            compressed_code (list of int): The list containing code values for
                                        characters/sequences.

        Returns:
            text (str): The decoded text, where code values are replaced with their
                    characters/sequences.
        """
        old = compressed_code[0]
        sequence = self.table[old]
        code = 256
        text = ""
        char = sequence[0]
        text += char
        for i in range(len(compressed_code)-1):
            new = compressed_code[i+1]
            if new not in self.table:
                sequence = self.table[old] + char
            else:
                sequence = self.table[new]
            text += sequence
            char = sequence[0]
            self.table[code] = self.table[old] + char
            code += 1
            old = new
        return text

    def decode_data(self, compressed_data_str):
        """Decode the code values from the compressed data.

        Args:
            compressed_data_str (str): The compressed codes as a string representing
                                    the binary data.

        Returns:
            data_array (list of int): A list containing the values for characters/sequences.
        """
        data_array = []
        for i in range(0, len(compressed_data_str), 12):
            char_bin = compressed_data_str[i:i+12]
            char_int = int(char_bin, 2)
            data_array.append(char_int)
        return data_array

    def parse_data(self, header_data):
        """Parse the compressed data from the given header data.

        Args:
            header_data (str): The binary data represented as a string.

        Returns:
            compressed_data (str): The compressed binary data represented as a string.
        """
        padding_len = header_data[:8]
        padding_len_base = int(padding_len, base=2)
        compressed_data = header_data[8+padding_len_base:]
        return compressed_data

    def decompress(self, binary_data_array):
        """ Decompress the data from the compressed file.

        This method initializes the table, parses the data given from the compressed file,
        decodes the code values from the parsed data and then decodes the values to their
        corresponding characters/sequences.

        Args:
            binary_data_array (str): The complete header data from the compressed file.

        Returns:
           decoded_text (str): The decoded text in ASCII format.
        """
        self._init_table(compress=False)
        header_data = self.parse_data(binary_data_array)
        decoded_data = self.decode_data(header_data)
        decoded_text = self.decode_text(decoded_data)
        return decoded_text

    def decompress_file(self):
        """Decompress the file given during initialization.

        This method decompresses the file given in the constructor. It reads the content of the
        file, decompresses the text and calls filehandler-object to write the text in bytearray
        format into the file.
        """
        binary_data_array = self.filehandler.read_binary_file()
        decoded_text = self.decompress(binary_data_array)
        self.filehandler.write_decoded_text_to_file(decoded_text)
