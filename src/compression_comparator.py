import time


class CompressionComparator():
    """This class is used for comparing the algorithms, including calling the compression
    and decompression methods of huffman coding algorithm and LZW-algorithm, 
    measuring their performance, reading and writing the data using FileHandler
    and providing the results to the UI for display.

    Attributes:
        filehandler (Filehandler): An instance of FileHandler that is responsible for handling
                                all file operations.
        original_file_size (bytes): The size of the file before compression in bytes.
    """

    def __init__(self, filehandler) -> None:
        """Create an instance of CompressionComparator.

        Args:
            filehandler (FileHandler): An instance of FileHandler to handle all file operations.
        """
        self.filehandler = filehandler
        self.original_file_size = self.filehandler.get_file_size()

    def benchmark(self, algorithm):
        """Run the compression and decompression methods for given algorithm
        and store results in the list.

        Args:
            algorithm (HuffmanCoding or LZW): An algorithm object to benchmark.

        Returns:
            benchmark_results (list): A list containing the compression statistics with the format
                                    [algorithm name, filename, filesize, compressed filesize,
                                    compression ratio, compression time, decompression time]
        """
        compression_stats = self.benchmark_compress(algorithm)
        decompression_stats = self.benchmark_decompress(algorithm)
        benchmark_results = compression_stats
        benchmark_results[6] = decompression_stats[6]

        return benchmark_results

    def compare(self, huffman, lzw):
        """Run the benchmark method for each algorithm and store the results in the
        compression stats list.

        Args:
            huffman (HuffmanCoding): An instance of HuffmanCoding algorithm.
            lzw (LZW): An instance of LZW algorithm.

        Returns:
            algorithm_stats (list): A list containing the compression statistics for each algorithm.
                                Each list element is a list with the format [algorithm name,
                                filename, filesize, compressed filesize, compression ratio,
                                compression time, decompression time]
        """

        compression_stats = []

        huffman = self.benchmark(huffman)
        lzw = self.benchmark(lzw)

        compression_stats.append(huffman)
        compression_stats.append(lzw)

        return compression_stats

    def benchmark_decompress(self, algorithm):
        """Run the decompress method for given algorithm and measure its performance.

        This method returns a list containing decompression statistics. The list includes:
        - The name of the algorithm
        - The name of the decompressed file
        - Decompression time in seconds


        If the decompressed file is exactly the same size as the original, the compression time
        compressed filesize and compression ratio are set to 0.0, as they are not measured in
        this method. If the decompressed file size differs from the original, all statistics are
        set to None, indicating a decompression error.

        Args:
            algorithm (HuffanCoding or LZW): An algorithm object to use for decompression.

        Returns:
            decompression_stats: A list containing the decompression statistics with the format
                                [algorithm name, filename, filesize, compressed filesize,
                                compression ratio, compression time, decompression time]

                                If the decompressed file is the same size as the original,
                                list type is [str, str, float, float, float, float, float],
                                otherwise [str, str, float, None, None, None, None].
        """
        decompression_stats = [
            algorithm.name, self.filehandler.filename, self.original_file_size / 1024]

        start_decompress_time = time.time()
        self.decompress(algorithm)
        end_decompress_time = time.time()
        decompression_time = end_decompress_time - start_decompress_time

        decompressed_file_size = self.filehandler.get_file_size()
        if decompressed_file_size == self.original_file_size:
            stats = (0.0, 0.0, 0.0, decompression_time)

        else:
            stats = (None, None, None, None)

        decompression_stats.extend(list(stats))
        return decompression_stats

    def benchmark_compress(self, algorithm):
        """Run the compress method for given algorithm and measure its performance.

        This method returns a list containing compression statistics. The list includes:
        - The name of the algorithm
        - The name of the compressed file
        - The size of the file in bytes
        - The size of the compressed file in bytes
        - Compression ratio %
        - Compression time in seconds

        The decompression time is set to 0.0, as it is not measured in this method.

        Args:
            algorithm (HuffanCoding or LZW): An algorithm to use for compression.

        Returns:
            compression_stats (list): A list type of [str, str, float, float, float, float, float]
                                    containing the compression statistics with the format
                                    [algorithm name, filename, filesize, compressed filesize,
                                    compression ratio, compression time, decompression time]
        """
        start_compress_time = time.time()
        self.compress(algorithm)
        end_compress_time = time.time()
        compression_stats = [
            algorithm.name, self.filehandler.filename, self.original_file_size / 1024]
        compression_time = end_compress_time - start_compress_time

        compressed_file_size = self.filehandler.get_file_size()
        compression_ratio = (1 - compressed_file_size /
                             self.original_file_size) * 100

        stats = (compressed_file_size / 1024,
                 compression_ratio, compression_time, 0.0)
        compression_stats.extend(list(stats))

        return compression_stats

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

        Before compression the name of the algorithm is checked.
        - If the chosen algorithm is "LZW", this method invokes the filehandler to read the file and
        check if it contains symbols outside the range of 0-255 unicode points. Any found symbol is
        added to the extra supported symbols list which is then returned to this method. The list
        containing the extra symbols is then given to the LZW algorithm.

        Args:
            algorithm (HuffmanCoding or LZW object): An algorithm object to use for compressing.
        """
        if algorithm.name == "LZW":
            supported = self.filehandler.find_extra_supported_symbols()
            algorithm.set_extra_supported_symbols(supported)

        text_to_compress = self.filehandler.read_file()
        compressed_text = algorithm.compress(text_to_compress)
        compressed_text_in_binary = self.convert_data_to_bytes(compressed_text)
        self.filehandler.write_data_to_binary_file(
            compressed_text_in_binary, algorithm.name)

    def decompress(self, algorithm):
        """Decompress the file given during initialization with chosen algorithm.

        This method decompresses the file given in the FileHandler constructor. It reads the
        content of the file, decompresses the text and calls FileHandler-object to write the text
        into the file.

        Args:
            algorithm (HuffmanCoding or LZW object): The algorithm object to use for decompressing.
        """
        compressed_data = self.filehandler.read_binary_file(algorithm.name)
        decoded_text = algorithm.decompress(compressed_data)
        self.filehandler.write_decoded_text_to_file(
            decoded_text, algorithm.name)
