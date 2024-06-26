import heapq
from utilities.utils import add_padding, calculate_min_bits_needed


class Node:
    """Class for nodes.

    Attributes:
        char: A character in a text.
        freq: The frequency of the char.
        left: The left child.
        right: The right child.
    """

    def __init__(self, character=None, freq=None):
        """Constructor that creates a new Node.

        Args:
            character: A character.
            freq: The frequency of the char.
        """
        self.char = character
        self.freq = freq
        self.left = None
        self.right = None

    def is_leaf_node(self):
        """Check if the current node is a leaf node.

        Returns:
            bool: True if the current node is a leaf node (it has no left child), False otherwise
        """
        return self.left is None

    def __lt__(self, other):
        """Compare nodes based on frequencies so that the
        lowest frequencies has higher priority.

        This is used to implement the min heap.

        Args:
            other: The other node to compare.

        Returns:
            bool: True if frequency is lower than other, False otherwise.
        """
        return self.freq < other.freq


class HuffmanCoding:
    """Class for huffman coding algorithm.

    Implements the Huffman coding algorithm for text compression and decompression.

    Attributes:
        bit_strings (dict): A dictionary mapping unique characters to their Huffman codes.
        reverse_bit_strings (dict): A dictionary mapping Huffman codes to their unique characters.
        root (Node): The root node of the Huffman tree.
        header (str): The header data as a string of binary data.
        name (str): The name of the algorithm.
        prev_compress (bool): Indicates whether compression has occurred previously.
        min_bits (int): The minimum bits needed to represents the length of the header.
        min_bits_char (int): The minimum bits needed to represents the largest unicode point value.
    """

    def __init__(self):
        """Create a new instance of Huffman coding algorithm."""
        self.bit_strings = {}
        self.reverse_bit_strings = {}
        self.root = None
        self.header = ""
        self.name = "Huffman"
        self.prev_compress = False
        self.min_bits = 0
        self.min_bits_char = 0

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

    def _find_largest_unicode_value(self, frequency_dict):
        """Find the largest unicode point value from the frequency dictionary of the
        characters in the text.

        Args:
            frequency_dict (dict): A dictionary where keys are characters found in the text
                                 and values are the frequencies of those characters.

        Returns:
            largest_value (int): The largest unicode point value from the dictionary.
        """
        largest_value = max(ord(key) for key in frequency_dict.keys())
        return largest_value

    def set_min_bits_char(self, min_bits):
        """Set min bits needed for representing the largest unicode point of the character.

        Args:
            min_bits (int): The minimum bits needed to represent the largest unicode point value.
        """
        self.min_bits_char = min_bits

    def get_min_bits_char(self):
        """Get minimum bits needed to represent the largest unicode point value.

        Returns:
            min_bits_char: The minimum bits needed to represent the largest unicode point value.
        """
        return self.min_bits_char

    def _calculate_and_set_min_bits_for_char(self, frequency):
        """Calculate and set min bits needed to represent the largest unicode point value of the
        character.

        This method calculates the minimum bits needed and rounds the value up to the nearest
        multiple of 8, and stores the value to the attribute "self.min_bits_char".

        Args:
            frequency (dict): A dictionary where keys are characters found in the text
                            and values are the frequencies of those characters.
        """
        max_unicode_point = self._find_largest_unicode_value(frequency)
        min_bits_needed = calculate_min_bits_needed(max_unicode_point)
        min_bits = self._round_min_bits_dividable_by_eight(min_bits_needed)
        self.set_min_bits_char(min_bits)

    def create_min_heap(self, frequency_dict) -> list:
        """Create nodes for each character and push those nodes onto a priority queue (min heap)
        based on their frequency values.

        Args:
            frequency_dict (dict): A dictionary where keys are characters found in the text
            and values are the frequencies of those characters.

        Returns:
            heap (list of Nodes): A min heap represented as a list of nodes.
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
        """Build a Huffman tree based on the characters and their frequencies in the text file.

        Constructs a Huffman tree by creating a dictionary of character's frequencies in the text, 
        and uses that to create a min heap and merges nodes with the lowest frequencies
        until only one is left.

        Args:
            text (str): text to be compressed/decompressed.

        Returns:
            root (Node): The root node of the constructed Huffman tree.
        """
        frequency = self.create_frequency_dict(text)
        self._calculate_and_set_min_bits_for_char(frequency)
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
            bit_strings (dict): A dictionary where keys are characters and values are the
                            constructed Huffman codes.
        """
        bit_string = ""
        self._create_bit_string(self.root, bit_string)

        return self.bit_strings

    def _create_bit_string(self, node, bit_string):
        """Recursively creates bit strings for each character.

        Creates a bit string for each character in the tree that represents its encoding.
        If the node is a leaf node (character), the bit string is stored.
        If the tree contains only one node, the bit string defaults to zero.
        If the node is an internal node, continue to its child nodes.

        If the node is a left child, 0 is added to the bit string.
        If the node is a right child, 1 is added to the bit string.

        Args:
            node (Node): The current node in the tree being processed.
            bit_string (str): The constructed bit string so far.

        Returns:
            None. Function traverses the tree recursively and updates the bit_strings and
            the reverse_bit_strings dictionaries.
        """
        if node.char is not None:
            if bit_string == "":
                bit_string = "0"
            self.bit_strings[node.char] = bit_string
            self.reverse_bit_strings[bit_string] = node.char
            return

        self._create_bit_string(node.left, bit_string + "0")
        self._create_bit_string(node.right, bit_string + "1")

    def encode_text(self, text):
        """Encode the given text using huffman codes.

        Args:
            text (str): The plain text to be encoded.

        Returns:
            encoded_text (str): The encoded text where characters are replaced
                            by their huffman codes.
        """
        encoded_text = ""
        for char in text:
            encoded_text += self.bit_strings[char]

        return encoded_text

    def encode_header(self, node):
        """Encode the generated huffman tree so it can be rebuilt and the data decoded.

        The header is encoded with the following logic:
        if node is a leaf:
            - add "1".
            - add binary representation of the character (in the length of minimum bits required to
            represent the largest unicode point value).
        Otherwise,
            - add "0".
            - encode recursively left and right child nodes.

        Args:
            node (Node): The root of the huffman tree.
        """
        if node.is_leaf_node():
            self.header += "1"
            self.header += format(ord(node.char), f"0{self.min_bits_char}b")
        else:
            self.header += "0"
            self.encode_header(node.left)
            self.encode_header(node.right)

    def set_min_bits_needed(self, bits_needed):
        """Set min_bits to the bits_needed.

        Args:
            bits_needed (int): The integer value of minimum bits needed to represent
                            the lenght of the header.
        """
        self.min_bits = bits_needed

    def get_min_bits_needed(self):
        """Get minimum bits needed.

        Returns:
            min_bits (int): The integer value of minimum bits needed to represent
                            the lenght of the header.
        """
        return self.min_bits

    def _round_min_bits_dividable_by_eight(self, value):
        """Round the minimum bits needed value to be dividable by 8.

        If the value is not dividable by 8, it is rounded up to the nearest multiple of 8.

        Args:
            value (int): The integer value to be round.

        Returns:
            value (int): The rounded integer value of minimum bits.
        """
        if value % 8 != 0:
            value += (8 - value % 8)
        return value

    def _calculate_and_set_min_bits(self):
        """Calculate and set the minimum bits needed to represent the lenght of the header.

        This method calculates the minimum bits needed and rounds the value up to the nearest
        multiple of 8, and stores the value to the attribute "self.min_bits".

        """
        min_bits_needed = calculate_min_bits_needed(len(self.header))
        min_bits = self._round_min_bits_dividable_by_eight(min_bits_needed)
        self.set_min_bits_needed(min_bits)

    def create_complete_data(self, text):
        """Create a complete data with a string representation of binary data.

        First this method calculates the minimum number of bits needed to represent the length
        of the header, and then creates the complete data.

        The complete data is formatted with the following logic:
            - Length of the header (minimum bits).
            - Length of the padding of the header (8 bits).
            - Length of the padding of the compressed data (8 bits).
            - Padded header data.
            - Compressed data.

        Args:
            text (str): The text to encode and create a header for.

        Returns:
            complete data (str): The complete data represented as a string of binary data.
        """
        self.header = ""
        encoded_text = self.encode_text(text)
        self.encode_header(self.root)
        len_encoded_text = len(encoded_text)

        length_header = len(self.header)
        self._calculate_and_set_min_bits()
        len_header_bin = format(length_header, f"0{self.min_bits}b")

        padding_len_header, padded_header = add_padding(
            self.header, length_header)
        padding_len_header_bin = format(padding_len_header, "08b")
        padding_len_data, padded_data = add_padding(
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
        then generates a complete data as a string of binary data representing that huffman tree.

        Args:
            text (str): The text to be compressed.

        Returns:
            complete_data (str): The complete data represented as a string of binary data.
        """

        self.build_huffman_tree(text)
        self.create_bit_strings_dict()
        complete_data = self.create_complete_data(text)
        self.prev_compress = True
        return complete_data

    def parse_int_from_binary(self, binary_string):
        """Parse integer value from the given binary string.

        Args:
            binary_string (str): The binary data represented as a string.

        Returns:
            value (int): The integer value of the given binary string.
        """
        value = int(binary_string, base=2)
        return value

    def parse_data(self, complete_data: str) -> tuple[str, str]:
        """Parse header data representing the huffman tree and the compressed data
        from the given complete data.

        Args:
            complete_data (str): The binary data represented as a string.

        Returns:
            tuple of (str, str): A tuple containing the header data and the compressed data.
        """

        len_of_header = self.parse_int_from_binary(
            complete_data[:self.min_bits])
        padding_len_of_header = self.parse_int_from_binary(
            complete_data[self.min_bits+1:self.min_bits+8])
        padding_len_of_compressed_data = self.parse_int_from_binary(
            complete_data[self.min_bits+8:self.min_bits+16])

        header_start_index = self.min_bits + 16 + padding_len_of_header
        header_end_index = self.min_bits + 16 + len_of_header + padding_len_of_header
        header_data = complete_data[header_start_index:header_end_index]

        compressed_data_starting_index = header_end_index + padding_len_of_compressed_data
        compressed_data = complete_data[compressed_data_starting_index:]

        return header_data, compressed_data

    def rebuild_huffman_tree(self, header: str, index: int) -> tuple[Node, int]:
        """Rebuild the huffman tree based on the header data.

        Args:
            header (str): A binary string representing the header data used to rebuild the tree.
            index (int): Pointing the current position of the the header data.

        Returns:
            tuple of (Node, int): A tuple containing the root of the tree and the next position
                                to process.
        """
        if index >= len(header):
            return None, index

        bit = header[index]
        index += 1

        if bit == "1":
            char_bits = header[index:index + self.min_bits_char]
            char = chr(int(char_bits, base=2))
            index += self.min_bits_char
            node = Node(char)
        else:
            left_node, index = self.rebuild_huffman_tree(header, index)
            right_node, index = self.rebuild_huffman_tree(header, index)
            node = Node()
            node.left = left_node
            node.right = right_node

        return node, index

    def decode_text(self, compressed_data: str, reverse_bit_strings: dict) -> str:
        """Decode the text from the compressed data by swapping the huffman codes with their
        corresponding characters.

        Args:
            compressed_data (str): The compressed data as a string representing the binary data.
            reverse_bit_strings (dictionary): A dictionary where keys are huffman codes and
                                            values are their characters.

        Returns:
            decoded_text (str): The decoded text in plain text.
        """
        decoded_text = ""
        sequence = ""

        for bit in compressed_data:
            sequence += bit

            if sequence in reverse_bit_strings:
                decoded_text += reverse_bit_strings[sequence]
                sequence = ""

        return decoded_text

    def decompress(self, complete_data: str) -> str:
        """Decompress the data from the compressed file.

        This function parses the data given from the compressed file, rebuilds the huffman tree
        and creates the dictionary mapping the  huffman codes and their characters, and then
        decodes the text using the rebuilt huffman tree. Finally, this method sets the attribute
        "self.prev_compress" to False.

        Args:
            complete_data (str): The complete data from the compressed file.

        Returns:
            decoded_text (str): The decoded text in plain text.
        """
        header_data, compressed_data = self.parse_data(complete_data)
        root, _ = self.rebuild_huffman_tree(header_data, 0)
        self.root = root
        self.create_bit_strings_dict()
        decoded_text = self.decode_text(
            compressed_data, self.reverse_bit_strings)
        self.prev_compress = False
        return decoded_text
