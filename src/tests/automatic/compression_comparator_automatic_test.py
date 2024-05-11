import unittest
import os
from compression_comparator import CompressionComparator
from utilities.filehandler import FileHandler
from utilities.utils import FILE_DIRECTORY, list_non_empty_text_files
from algorithms.huffman import HuffmanCoding
from algorithms.lzw import LZW


class TestCompressionComparatorAutomatic(unittest.TestCase):
    def setUp(self):
        self.all_text_files = list_non_empty_text_files()

    def _tear_down(self, filehandler):
        filehandler.tear_down()
        files = [file for file in os.listdir(
            FILE_DIRECTORY) if file.endswith(".bin")]
        for file in files:
            os.remove(os.path.join(FILE_DIRECTORY, file))

    def _test_benchmark_compress(self, comparator, algorithm):
        result = comparator.benchmark_compress(algorithm)
        return result

    def _test_benchmark_decompress(self, comparator, algorithm):
        result = comparator.benchmark_decompress(algorithm)
        return result

    def _test_benchmark_compress_and_decompress(self, algorithm, comparator):
        original_size = comparator.filehandler.get_file_size() / 1024
        compression_results = self._test_benchmark_compress(
            comparator, algorithm)
        compressed_file_size = comparator.filehandler.get_file_size() / 1024
        decompression_time_before = compression_results[6]
        decompression_results = self._test_benchmark_decompress(
            comparator, algorithm)

        self.assertEqual(compression_results[0], algorithm.name)
        self.assertEqual(
            compression_results[1], comparator.filehandler.filename)
        self.assertEqual(compression_results[2], original_size)
        self.assertEqual(compression_results[3], compressed_file_size)
        self.assertNotEqual(compression_results[4], None)
        self.assertGreater(compression_results[5], 0.0)
        self.assertEqual(decompression_time_before, 0.0)

        self.assertEqual(decompression_results[0], algorithm.name)
        self.assertEqual(
            decompression_results[1], comparator.filehandler.filename)
        self.assertEqual(decompression_results[2], original_size)
        self.assertEqual(decompression_results[3], 0.0)
        self.assertEqual(decompression_results[4], 0.0)
        self.assertGreater(decompression_results[6], decompression_time_before)

    def test_benchmark_all_files_huffman(self):
        for file in self.all_text_files:
            filename = file[1]
            filehandler = FileHandler(filename)
            huffman = HuffmanCoding()
            comparator = CompressionComparator(filehandler)
            self._test_benchmark_compress_and_decompress(huffman, comparator)

        self._tear_down(filehandler)

    def test_benchmark_all_files_lzw(self):
        for file in self.all_text_files:
            filename = file[1]
            filehandler = FileHandler(filename)
            lzw = LZW()
            comparator = CompressionComparator(filehandler)
            self._test_benchmark_compress_and_decompress(lzw, comparator)

        self._tear_down(filehandler)