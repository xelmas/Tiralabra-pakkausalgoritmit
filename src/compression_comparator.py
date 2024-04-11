
class CompressionComparator():
    """This class is used for comparing the algorithms, including calling the compression
    and decompression methods of huffman coding algorithm and LZW-algorithm, 
    measuring their performance, and providing the results to the UI for display.
    """

    def __init__(self, huffman, lzw) -> None:

        self.huffman = huffman
        self.lzw = lzw

    def compare(self):
        pass

    def compress(self, algorithm):
        algorithm.compress_file()

    def decompress(self, algorithm):
        algorithm.decompress_file()
