import heapq


class Node:
    """Class for nodes.

    Attributes:
        char: character in a text.
        freq: frequency of the char.
        left: left child.
        right: right child.
    """

    def __init__(self, character, freq):
        """Constructor that creates a new node.

        Args:
            character: character.
            freq: frequency of the char.
        """
        self.char = character
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """Compare nodes based on frequencies so that the
        lowest frequencies has higher priority.

        This is used to implement the min heap.

        Args:
            other: other node to compare.

        Returns:
            Boolean: True if frequency is lower than other, otherwise False.
        """
        return self.freq < other.freq


class HuffmanCoding:
    """Class for huffman coding algorithm.

    Implements the Huffman coding algorithm for text compression and decompression.

    Attributes:
        path (str): The path to the text file used for compression/decompression.
        bit_strings (dict): A dictionary mapping unique characters to their Huffman codes.
        root (Node): The root node of the Huffman tree.
    """

    def __init__(self, path):
        """Create a new instance of Huffman coding algorithm.

        Args:
            path (str): A path to the text file to be compressed/decompressed.
        """
        self.path = path
        self.bit_strings = {}
        self.root = None

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

    def read_file(self):
        """Read a file and return its contents as a string.

        Returns:
            text (str): A string that contains the content of the file.
        """
        with open(self.path, "r", encoding="utf-8") as file:
            text = file.read()
        return text

    # function to help debugging
    def print_huffman_tree(self, root, level=0):
        if root is not None:
            self.print_huffman_tree(root.right, level + 1)
            print(" " * 5 * level + "-->", root.char, root.freq)
            self.print_huffman_tree(root.left, level + 1)

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

        """
        bit_string = ""
        self.create_bit_string(self.root, bit_string)

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

    def compress(self):
        # output_file = "text" + ".bin"
        text = self.read_file()
        self.build_huffman_tree(text)
        self.create_bit_strings_dict()
        print("Frequencies:", self.create_frequency_dict(text))
        print("Bit strings: ", self.bit_strings)
        self.print_huffman_tree(self.root)
        print("Compressed")
