import heapq


class Node:
    """Class for nodes.

    Attributes:
        char: A character in a text.
        freq: The frequency of the char.
        left: The left child.
        right: The right child.
    """

    def __init__(self, character=None, freq=None):
        """Constructor that creates a new node.

        Args:
            character: A character.
            freq: The frequency of the char.
        """
        self.char = character
        self.freq = freq
        self.left = None
        self.right = None

    def is_leaf_node(self):
        return self.left is None

    def __lt__(self, other):
        """Compare nodes based on frequencies so that the
        lowest frequencies has higher priority.

        This is used to implement the min heap.

        Args:
            other: The other node to compare.

        Returns:
            Boolean: True if frequency is lower than other, otherwise False.
        """
        return self.freq < other.freq


class HuffmanCoding:
    """Class for huffman coding algorithm.

    Implements the Huffman coding algorithm for text compression and decompression.

    Attributes:
        filehandler (FileHandler): The FileHandler object provided during initialization.
        bit_strings (dict): A dictionary mapping unique characters to their Huffman codes.
        root (Node): The root node of the Huffman tree.
    """

    def __init__(self, filehandler):
        """Create a new instance of Huffman coding algorithm.

        Args:
            filehandler (FileHandler): An instance of the FileHandler class.
        """
        self.filehandler = filehandler
        self.bit_strings = {}
        self.root = None
        self.header = ""

    def create_frequency_dict(self, text):
        """Calculate the frequencies of characters in a text and return a dictionary.

        Args:
            text (str): The text to calculate for character frequencies.

        Returns:
            frequency (dict): A dictionary where keys are characters found in the text
            and values are the frequencies of those characters.
        """
        frequency = {}
        for char in text:
            if char not in frequency:
                frequency[char] = 0
            frequency[char] += 1
        return frequency

    def create_min_heap(self, frequency_dict):
        """Create nodes for each character and push those nodes onto a priority queue (min heap)
        based on their frequency values.

        Args:
            frequency_dict (dict): A dictionary where keys are characters found in the text
            and values are the frequencies of those characters.

        Returns:
            heap: A min heap of nodes.
        """
        heap = []
        heapq.heapify(heap)
        for symbol in frequency_dict:
            node = Node(symbol, frequency_dict[symbol])
            heapq.heappush(heap, node)

        return heap

    def merge_nodes(self, heap):
        """Merge nodes with the lowest frequency values until only one node remains. 

        Starting from the lowest frequency values, repeatedly merge two nodes together
        and push that new node to the min heap. This is done until there is only one node left, 
        which is the root of the Huffman tree.

        Args:
            heap: A min heap of nodes.

        Returns:
            root (Node): A root of the Huffman tree.
        """
        while len(heap) > 1:

            node1 = heapq.heappop(heap)
            node2 = heapq.heappop(heap)

            merged = Node(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(heap, merged)

        self.root = heap[0]
        return self.root

    def build_huffman_tree(self, text):
        """Build a Huffman tree based on the text file.

        Constructs a Huffman tree by creating a dictionary of character's frequencies in the text, 
        and uses that to create a min heap and merges nodes with the lowest frequencies
        until only one is left.

        Args:
            text (str): text to be compressed/decompressed.

        Returns:
            root (Node): The root node of the constructed Huffman tree.
        """
        frequency = self.create_frequency_dict(text)
        min_heap = self.create_min_heap(frequency)
        self.merge_nodes(min_heap)
        return self.root

    def create_bit_strings_dict(self):
        """Create a dictionary mapping characters to their Huffman codes.

        This function constructs a dictionary where keys are characters 
        and values are the constructed Huffman codes. 
        The actual creation is performed by the helper function create_bit_string,
        which recursively traverses the Huffman tree starting from the root.

        This function passes the root node and an empty bit string to the 
        create_bit_string function. That function traverses the tree until it reaches the leaf node.
        It adds 0 if the current node is the left child node, and adds 1 if the current node is
        the right child node. When a leaf node is reached, the constructed bit string is 
        stored in the dictionary.

        Returns:
            (dict):  A dictionary where keys are characters and values are 
                    the constructed Huffman codes.
        """
        bit_string = ""
        self.create_bit_string(self.root, bit_string)
        return self.bit_strings

    def create_bit_string(self, node, bit_string):
        """Recursively creates bit strings for each character.

        Creates a bit string for each character in the tree that represents its encoding.
        If the node is a leaf node (character), the bit string is stored.
        If the node is an internal node, continue to its child nodes.

        If the node is a left child, 0 is added to the bit string.
        If the node is a right child, 1 is added to the bit string.

        Args:
            node (Node): The current node in the tree being processed.
            bit_string (str): The constructed bit string so far.

        Returns:
            None. Function traverses the tree recursively and updates the bit_strings dictionary.
        """
        if node.char is not None:
            self.bit_strings[node.char] = bit_string
            return

        self.create_bit_string(node.left, bit_string + "0")
        self.create_bit_string(node.right, bit_string + "1")

    def encode_text(self, text):
        """Encode the given text using huffman codes.

        Args:
            text (str): The text in ASCII format to be encoded.

        Returns:
            str: The encoded text where characters are replaced by their huffman codes.
        """
        encoded_text = ""
        for char in text:
            encoded_text += self.bit_strings[char]

        return encoded_text

    def convert_header_data_to_bytes(self, header_data):
        """Convert a string of header data to bytes.

        Args:
            header_data (str): The string of header data to be converted.

        Returns:
            encoded_bytes (bytearray): The converted data as an array of bytes.
        """
        encoded_bytes = bytearray()
        for i in range(0, len(header_data), 8):
            byte = header_data[i:i+8]
            byte_value = int(byte, 2)
            encoded_bytes.append(byte_value)

        return encoded_bytes

    def encode_header(self, node):
        """Encode the generated huffman tree so it can be rebuilt and the data decoded.

        The header is encoded with the following logic:
        if node is a leaf:
            - add "1".
            - add binary representation of the character in 8 bits.
        Otherwise,
            - add "0".
            - encode recursively left and right child nodes.

        Args:
            node (Node): The root of the huffman tree.
        """
        if node.is_leaf_node():
            self.header += "1"
            self.header += format(ord(node.char), "08b")
        else:
            self.header += "0"
            self.encode_header(node.left)
            self.encode_header(node.right)

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

    def create_header(self, text):
        """Create a complete header data with a string representation of binary data.

        The data is formatted with the following logic:
            - Length of the header (16 bits).
            - Length of the padding of the header (8 bits).
            - Length of the padding of the compressed data (8 bits).
            - Padded header data.
            - Compressed data.

        Args:
            text (str): The text to encode and create a header for.

        Returns:
            complete data (str): The complete data represented as a string of binary data.
        """
        encoded_text = self.encode_text(text)
        self.encode_header(self.root)

        length_header = len(self.header)
        len_encoded_text = len(encoded_text)
        len_header_bin = format(length_header, "016b")

        padding_len_header, padded_header = self._add_padding(
            self.header, length_header)
        padding_len_header_bin = format(padding_len_header, "08b")

        padding_len_data, padded_data = self._add_padding(
            encoded_text, len_encoded_text)
        padding_len_data_bin = format(padding_len_data, "08b")

        data_array = []

        data_array.append(len_header_bin)
        data_array.append(padding_len_header_bin)
        data_array.append(padding_len_data_bin)

        data_array.append(padded_header)
        data_array.append(padded_data)

        complete_data = "".join(data for data in data_array)
        return complete_data

    def compress(self, text):
        """Compress the text using Huffman-coding algorithm.

        This method builds the huffman tree, creates a dictionary mapping the huffman codes and
        then generates a bytearray header representing that huffman tree.

        Args:
            text (str): The text to be compressed.

        Returns:
            header_in_binary (bytearray): The header data represented as a bytearray.
        """

        self.build_huffman_tree(text)
        self.create_bit_strings_dict()
        header_data = self.create_header(text)
        compressed_header_in_binary = self.convert_header_data_to_bytes(
            header_data)
        return compressed_header_in_binary

    def compress_file(self):
        """Compress the file given during initialization.

        This method compresses the file given in the constructor. It reads the content of the file,
        compresses the text and calls filehandler-object to write the text in bytearray format
        into the file.
        """
        text = self.filehandler.read_file()
        compressed_text = self.compress(text)
        self.filehandler.write_data_to_binary_file(compressed_text)

    def parse_data(self, compressed_data_str):
        """Parse header data representing the huffman tree and the compressed data
        from the given complete header data.

        Args:
            compressed_data_str (str): The binary data represented as a string.

        Returns:
            tuple of (str, str): A tuple containing the header data and the compressed data.
        """
        len_header = compressed_data_str[:16]
        len_header_base = int(len_header, base=2)

        padding_len_header = compressed_data_str[17:24]
        padding_len_header_base = int(padding_len_header, base=2)

        padding_len_data = compressed_data_str[24:32]
        padding_len_data_base = int(padding_len_data, base=2)

        header_data = compressed_data_str[32+padding_len_header_base:32 +
                                          len_header_base+padding_len_header_base]
        compressed_data = compressed_data_str[32+len_header_base +
                                              padding_len_header_base+padding_len_data_base:]

        return header_data, compressed_data

    def rebuild_huffman_tree(self, header, index):
        """Rebuild the huffman tree based on the header data.

        Args:
            header (str): A string representing binary data.
            index (int): Pointing the current position of header data.

        Returns:
            tuple of (Node, int): A tuple containing the root of the tree and the index.
        """
        if index >= len(header):
            return None, index

        bit = header[index]
        index += 1

        if bit == "1":
            char_bits = header[index:index + 8]
            char = chr(int(char_bits, base=2))
            index += 8
            node = Node(char)
        else:
            left_node, index = self.rebuild_huffman_tree(header, index)
            right_node, index = self.rebuild_huffman_tree(header, index)
            node = Node()
            node.left = left_node
            node.right = right_node

        return node, index

    def decode_text(self, compressed_data, huffman_codes):
        """Decode the text from the compressed data by swapping the huffman codes with their
        corresponding characters.

        Args:
            compressed_data (str): The compressed text as a string representing the binary data.
            huffman_codes (dictionary): A dictionary where keys are characters and values are 
                    the constructed Huffman codes.

        Returns:
            str: The decoded text in ASCII format.
        """
        decoded_text = ""
        sequence = ""

        for bit in compressed_data:
            sequence += bit

            for char, code in huffman_codes.items():
                if sequence == code:
                    decoded_text += char
                    sequence = ""
                    break
        return decoded_text

    def decompress(self, compressed_data_str):
        """Decompress the data from the compressed file.

        This function parses the data given from the compressed file, rebuilds the huffman tree
        and creates the dictionary mapping the characters and their huffman codes, and then
        decodes the text using the rebuilt huffman tree.

        Args:
            compressed_data_str (str): The complete header data from the compressed file.

        Returns:
            decoded_text (str): The decoded text in ASCII format.
        """
        header_data, compressed_data = self.parse_data(compressed_data_str)
        root, _ = self.rebuild_huffman_tree(header_data, 0)
        self.root = root
        huffman_codes = self.create_bit_strings_dict()
        decoded_text = self.decode_text(compressed_data, huffman_codes)
        return decoded_text

    def decompress_file(self):
        """Decompress the file given during initialization.

        This method decompresses the file given in the constructor. It reads the content of the
        file, decompresses the text and calls filehandler-object to write the text in bytearray
        format into the file.
        """
        compressed_data_str = self.filehandler.read_binary_file()
        decoded_text = self.decompress(compressed_data_str)
        self.filehandler.write_decoded_text_to_file(decoded_text)
