
class CompressionComparator():
    """This class orchestrates the comparison process, including calling the compression and decompression methods 
    of Algorithm1 and Algorithm2, measuring their performance, and providing the results to the UI for display.
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