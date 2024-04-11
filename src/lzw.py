
class LZW():
    """Class for Lempel-Ziv-Welch algorithm.
    """

    def __init__(self, filehandler) -> None:
        self.table = None
        self.filehandler = filehandler

    def _init_table(self, compress=True):
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
        return self.table

    def encode(self, text_stream):
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
        encoded_bytes = bytearray()
        for i in range(0, len(header), 8):
            byte = header[i:i+8]
            byte_value = int(byte, 2)
            encoded_bytes.append(byte_value)
        return encoded_bytes

    def compress(self, text):
        self._init_table(compress=True)
        encoded_text_array = self.encode(text)
        header_str = self.create_header(encoded_text_array)
        compressed_header_in_binary = self.convert_data_to_bytes(header_str)
        return compressed_header_in_binary
        
    def compress_file(self):
        text = self.filehandler.read_file()
        header_in_binary = self.compress(text)
        self.filehandler.write_data_to_binary_file(header_in_binary)

    def decode(self, compressed_code):
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

    def decode_text(self, compressed_data_str):
        data_array = []
        for i in range(0, len(compressed_data_str), 12):
            char_bin = compressed_data_str[i:i+12]
            char_int = int(char_bin, 2)
            data_array.append(char_int)
        return data_array

    def parse_data(self, header_data):
        padding_len = header_data[:8]
        padding_len_base = int(padding_len, base=2)
        compressed_data = header_data[8+padding_len_base:]
        return compressed_data

    def decompress(self, binary_data_array):
        self._init_table(compress=False)
        header_data = self.parse_data(binary_data_array)
        decoded_data = self.decode_text(header_data)
        decoded_text = self.decode(decoded_data)
        return decoded_text
    
    def decompress_file(self):
        binary_data_array = self.filehandler.read_binary_file()
        decoded_text = self.decompress(binary_data_array)
        self.filehandler.write_decoded_text_to_file(decoded_text)
