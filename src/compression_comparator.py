import time


class CompressionComparator():
    """This class is used for comparing the algorithms, including calling the compression
    and decompression methods of huffman coding algorithm and LZW-algorithm, 
    measuring their performance, reading and writing the data using FileHandler
    and providing the results to the UI for display.
    """

    def __init__(self, filehandler) -> None:
        self.filehandler = filehandler

    def compare(self, huffman, lzw):
        compression_stats = []

        huffman_stats = ["Huffman"]
        huffman_stats.extend(list(self.benchmark(huffman)))
        compression_stats.append(huffman_stats)

        lzw_stats = ["LZW"]
        lzw_stats.extend(list(self.benchmark(lzw)))
        compression_stats.append(lzw_stats)

        return compression_stats

    def benchmark(self, algorithm):
        original_file_size = self.filehandler.get_file_size()

        start_compress_time = time.time()
        self.compress(algorithm)
        end_compress_time = time.time()
        compression_time = end_compress_time - start_compress_time
        compressed_file_size = self.filehandler.get_file_size()

        compression_ratio = compressed_file_size / original_file_size

        start_decompress_time = time.time()
        self.decompress(algorithm)
        end_decompress_time = time.time()
        decompression_time = end_decompress_time - start_decompress_time
        decompressed_file_size = self.filehandler.get_file_size()

        if decompressed_file_size == original_file_size:
            return compression_time, decompression_time, compression_ratio

        return None

    def convert_data_to_bytes(self, header_data):
        """Convert a binary string to bytes.

        This method converts a string of binary data into an array of bytes,
        enabling that the data can be written into the file.

        Args:
            header_data (str): The string of binary data to be converted.

        Returns:
            encoded_bytes (bytearray): The converted data as an array of bytes.
        """
        encoded_bytes = bytearray()
        for i in range(0, len(header_data), 8):
            byte = header_data[i:i+8]
            byte_value = int(byte, 2)
            encoded_bytes.append(byte_value)
        return encoded_bytes

    def compress(self, algorithm):
        """Compress the file given during initialization with chosen algorithm.

        This method compresses the file given in the FileHandler constructor. It reads the
        content of the file, compresses the text, converts the text into a writable binary format
        and then calls a FileHandler object to write it into the file.

        Args:
            algorithm (HuffmanCoding or LZW object): The algorithm object to use for decompressing.
        """
        text_to_compress = self.filehandler.read_file()
        compressed_text = algorithm.compress(text_to_compress)
        compressed_text_in_binary = self.convert_data_to_bytes(compressed_text)
        self.filehandler.write_data_to_binary_file(compressed_text_in_binary)

    def decompress(self, algorithm):
        """Decompress the file given during initialization with chosen algorithm.

        This method decompresses the file given in the FileHandler constructor. It reads the
        content of the file, decompresses the text and calls FileHandler-object to write the text
        into the file.

        Args:
            algorithm (HuffmanCoding or LZW object): The algorithm object to use for decompressing.
        """
        compressed_data = self.filehandler.read_binary_file()
        decoded_text = algorithm.decompress(compressed_data)
        self.filehandler.write_decoded_text_to_file(decoded_text)
