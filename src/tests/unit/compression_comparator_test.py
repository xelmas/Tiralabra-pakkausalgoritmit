import unittest
import os
from compression_comparator import CompressionComparator
from utilities.filehandler import FileHandler
from utilities.utils import FILE_DIRECTORY, list_non_empty_text_files
from algorithms.huffman import HuffmanCoding
from algorithms.lzw import LZW


class TestCompressionComparator(unittest.TestCase):
    def setUp(self):
        self.all_text_files = list_non_empty_text_files()

    def _tear_down(self, filehandler):
        filehandler.tear_down()
        files = [file for file in os.listdir(
            FILE_DIRECTORY) if file.endswith(".bin")]
        for file in files:
            os.remove(os.path.join(FILE_DIRECTORY, file))

    def test_compare(self):
        filename = self.all_text_files[0][1]
        filehandler = FileHandler(filename)
        comparator = CompressionComparator(filehandler)
        huffman = HuffmanCoding()
        lzw = LZW()
        compression_stats = comparator.compare(huffman, lzw)

        huffman_stats = compression_stats[0]
        self.assertEqual(huffman_stats[0], huffman.name)
        self.assertEqual(huffman_stats[1], filename)
        self.assertEqual(round(huffman_stats[2], 4), 895.7832)
        self.assertEqual(round(huffman_stats[3], 4), 471.2871)
        self.assertEqual(round(huffman_stats[4], 4), 47.3883)
        self.assertGreater(huffman_stats[5], 0.0)
        self.assertGreater(huffman_stats[6], 0.0)

        lzw_stats = compression_stats[1]
        self.assertEqual(lzw_stats[0], lzw.name)
        self.assertEqual(lzw_stats[1], filename)
        self.assertEqual(round(lzw_stats[2], 4), 895.7832)
        self.assertEqual(round(lzw_stats[3], 4), 375.9473)
        self.assertEqual(round(lzw_stats[4], 4), 58.0314)
        self.assertGreater(lzw_stats[5], 0.0)
        self.assertGreater(lzw_stats[6], 0.0)

    def test_benchmark_decompress_returns_None_after_decompression_error_huffman(self):
        filename = self.all_text_files[0][1]
        filehandler = FileHandler(filename)
        comparator = CompressionComparator(filehandler)
        huffman = HuffmanCoding()
        comparator.benchmark_compress(huffman)
        comparator.original_file_size = 800.00
        decompression_results = comparator.benchmark_decompress(huffman)
        self.assertEqual(decompression_results[3], None)
        self.assertEqual(decompression_results[4], None)
        self.assertEqual(decompression_results[5], None)
        self.assertEqual(decompression_results[6], None)
        self._tear_down(filehandler)

    def test_benchmark_decompress_returns_None_after_decompression_error_lzw(self):
        filename = self.all_text_files[0][1]
        filehandler = FileHandler(filename)
        comparator = CompressionComparator(filehandler)
        lzw = LZW()
        comparator.benchmark_compress(lzw)
        comparator.original_file_size = 800.00
        decompression_results = comparator.benchmark_decompress(lzw)
        self.assertEqual(decompression_results[3], None)
        self.assertEqual(decompression_results[4], None)
        self.assertEqual(decompression_results[5], None)
        self.assertEqual(decompression_results[6], None)
        self._tear_down(filehandler)

    def test_list_only_non_empty_text_files(self):
        for file in self.all_text_files:
            path = os.path.join(FILE_DIRECTORY, file[1])
            size = os.path.getsize(path)
            self.assertGreater(size, 0)

    def test_list_only_text_files(self):
        filename = self.all_text_files[0][1]
        filehandler = FileHandler(filename)
        comparator = CompressionComparator(filehandler)
        huffman = HuffmanCoding()
        comparator.benchmark_compress(huffman)
        text_files = list_non_empty_text_files()

        for file in text_files:
            self.assertTrue(file[1].endswith(".txt"))

        self._tear_down(filehandler)