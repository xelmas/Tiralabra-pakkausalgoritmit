from utilities.utils import add_padding, calculate_min_bits_needed


class LZW():
    """Class for Lempel-Ziv-Welch algorithm.

    Implements the LZW-algorithm for text compression and decompression.

    Attributes: 
        table (dict): The dictionary for characters and their corresponding code values.
        name (str): The name of the algorithm.
        extra_supported_symbols (list): The additional symbols to extend the dictionary.
        min_bits (int): The minimum bits needed to represents the biggest value.
        prev_compress (bool): Indicates whether compression has occurred previously.
    """

    def __init__(self) -> None:
        """Create a new instance of LZW-algorithm. """

        self.table = None
        self.name = "LZW"
        self.extra_supported_symbols = []
        self.min_bits = 0
        self.prev_compress = False

    def _init_table(self, compress=True):
        """Initialize the dictionary for mapping characters and their corresponding code values.

        This method initializes the mapping table for characters and codes within the range of
        0-255. Additionally all symbols in the extra_supported_symbols list is added to the table
        with the codes starting from 256.

        Method initializes the table based on the boolean value given:
        - If the value is true, table is initialized for compression, and then the keys are 
        characters and values are their codes in the dictionary.
        - If the value is False, table is initialized for decompression, and then the keys are
        codes and values are their corresponding characters.

        The constructed dictionary is stored in the variable self.table.

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

        code = 256
        for extra_symbol in self.extra_supported_symbols:
            if compress:
                table[extra_symbol] = code
            else:
                table[code] = extra_symbol
            code += 1

        self.table = table

    def set_extra_supported_symbols(self, supported_symbols):
        """Set extra supported symbols to the given list.

        Args:
            supported_symbols (list): A list containing all the symbols outside the range of
                                    0-255 unicode points that are found in the text.
        """
        self.extra_supported_symbols = supported_symbols

    def get_table(self) -> dict:
        """Return the initialized dictionary for characters and their corresponding code values.

        Returns:
            table (dict): The dictionary for mapping characters and their code values.
        """
        return self.table

    def encode(self, text_stream: str) -> list:
        """Encode the given text by replacing the characters with their code values.

        This method processes the text stream and updates the dictionary that keeps track of the
        characters/sequences and their codes. When the encoding starts, there are all possible
        single characters in the table mapped with their code values. As the text stream is
        processed, new sequences are added to the table and the code value is raised by one.
        The list containing encoded text is constructed at the same time, adding the code value for
        character/sequence to it.

        Args:
            text_stream (str): The plain text to be encoded.

        Returns:
            encoded_text (list): The encoded text as a list, where characters/sequences are 
                                replaced with their code values.
        """
        first_char = text_stream[0]
        index = 0
        code = 256 + len(self.extra_supported_symbols)
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

    def create_header(self, code_values: list) -> str:
        """Create a complete header data with a string representation of binary data.

        This method calculates the minimum number of bits needed to represent the biggest value in
        the table. It then converts each code value in the "code_values" list to a binary
        representation with the minimum required length and concatenates them into a single string.

        The add_padding method is called to add padding to the binary string. That method returns
        tuple containing the length of the padding, the padded binary string. These are then added
        to the data_array list. Finally, the contents of the data_array list are concatenated into
        a single string to form the complete data.

        The complete data includes:
        - The length of the padding of the data (in 8 bits)
        - The padded binary data

        Args:
            code_values (list): The encoded text as a list, where characters/sequences are 
                                replaced with their code values.

        Returns:
            complete data (str): The complete data represented as a string of binary data.
        """
        max_value = max(self.table.values())
        self.min_bits = calculate_min_bits_needed(max_value)

        binary_string = "".join(
            format(code_value, f"0{self.min_bits}b") for code_value in code_values)
        length_data = len(binary_string)
        len_header = length_data + 8
        padding_len, padded_data = add_padding(binary_string, len_header)
        padding_len_bin = format(padding_len, "08b")

        data_array = []
        data_array.append(padding_len_bin)
        data_array.append(padded_data)
        complete_data = "".join(data for data in data_array)

        return complete_data

    def set_min_bits_needed(self, bits_needed):
        """Set min_bits to the bits_needed.

        Args:
            bits_needed (int): The integer value of minimum bits needed to represent
                            the biggest value.
        """
        self.min_bits = bits_needed

    def get_min_bits_needed(self):
        """Get minimum bits needed.

        Returns:
            min_bits (int): The integer value of minimum bits needed to represent
                            the biggest value.
        """
        return self.min_bits

    def compress(self, text) -> str:
        """Compress the text using the LZW-algorithm.

        This method initializes the table, encodes the text, generates a header as a string of
        binary data that represents the compressed data, and sets the attribute "self.prev_compress"
        to True.

        Args:
            text (str): The text to compress.

        Returns:
            complete_data (str): The compressed data represented as a string of binary data.
        """

        self._init_table(compress=True)
        encoded_text = self.encode(text)
        complete_data = self.create_header(encoded_text)
        self.prev_compress = True
        return complete_data

    def decode_text(self, compressed_codes: list) -> str:
        """Decode the compressed codes to text.

        When the decoding starts, there are all possible single characters in the table mapped
        with their code values. While decoding is processed, the table is updated for each
        character. The text is decoded by reading the compressed codes and replacing them with
        their corresponding characters/sequences.

        Args:
            compressed_code (list of int): The list containing code values for
                                        characters/sequences.

        Returns:
            text (str): The decoded text, where code values are replaced with their
                    characters/sequences.
        """
        old = compressed_codes[0]
        sequence = self.table[old]
        code = 256 + len(self.extra_supported_symbols)
        text = ""
        char = sequence[0]
        text += char
        for i in range(len(compressed_codes)-1):
            new = compressed_codes[i+1]
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

    def decode_data(self, compressed_data: str) -> list:
        """Decode the code values from the compressed data.

        Args:
            compressed_data (str): The compressed codes as a string representing the binary data.
                                Each code is represented with the minimum length of bits.

        Returns:
            code_values (list of int): A list containing the values for characters/sequences.
        """
        code_values = []
        for i in range(0, len(compressed_data), self.min_bits):
            char_bin = compressed_data[i:i+self.min_bits]
            char_int = int(char_bin, 2)
            code_values.append(char_int)

        return code_values

    def parse_data(self, complete_data: str) -> str:
        """Parse the compressed data from the given complete data.

        The complete data includes:
        - The length of the padding of the data (8 bits)
        - The padded data

        Args:
            complete_data (str): The binary data represented as a string.

        Returns:
            compressed_data (str): The compressed binary data represented as a string.
        """
        padding_len = complete_data[:8]
        padding_len_base = int(padding_len, base=2)
        compressed_data = complete_data[8+padding_len_base:]

        return compressed_data

    def decompress(self, binary_data: str) -> str:
        """Decompress the data from the compressed file.

        This method initializes the table, parses the data given from the compressed file,
        decodes the code values from the parsed data and then decodes the values to their
        corresponding characters/sequences.

        Args:
            binary_data (str): The complete header data from the compressed file.

        Returns:
           decoded_text (str): The decoded text in plain text format.
        """
        self._init_table(compress=False)
        compressed_data = self.parse_data(binary_data)
        decoded_data = self.decode_data(compressed_data)
        decoded_text = self.decode_text(decoded_data)
        self.prev_compress = False

        return decoded_text
