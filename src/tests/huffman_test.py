import unittest
from huffman import HuffmanCoding
import heapq


class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.huffman = HuffmanCoding("src/tests/testfile.txt")
        self.text = self.huffman.file_handler.read_file()
        self.freq = self.huffman.create_frequency_dict(self.text)

    def test_creating_frequency_dict(self):
        freq2 = {"A": 6, "B": 1, "C": 6, "D": 2, "E": 5, }
        self.assertDictEqual(self.freq, freq2)

    def test_creating_min_heap(self):
        min_heap = self.huffman.create_min_heap(self.freq)
        lowest_prio_char = heapq.heappop(min_heap).char
        self.assertEqual(lowest_prio_char, "B")

    def test_merge_nodes(self):
        min_heap = self.huffman.create_min_heap(self.freq)
        self.huffman.merge_nodes(min_heap)
        root_freq_value = heapq.heappop(min_heap).freq
        self.assertEqual(root_freq_value, 20)

    def test_build_huffman_tree(self):
        root = self.huffman.build_huffman_tree(self.text)
        self.assertEqual(root.freq, 20)

    def test_create_bit_strings_dict(self):
        self.huffman.build_huffman_tree(self.text)
        self.huffman.create_bit_strings_dict()
        bit_strings_dict = self.huffman.bit_strings
        expected_dict = {"B": "000", "D": "001",
                         "E": "01", "A": "10", "C": "11"}
        self.assertDictEqual(bit_strings_dict, expected_dict)

    def test_encode_text(self):
        expected = "1010101010100001111111111110010010101010101"
        self.huffman.build_huffman_tree(self.text)
        self.huffman.create_bit_strings_dict()
        encoded_text = self.huffman.encode_text(self.text)
        self.assertEqual(encoded_text, expected)

    def test_encode_header(self):
        expected = "0001010000101010001001010001010101000001101000011"
        self.huffman.build_huffman_tree(self.text)
        self.huffman.encode_header(self.huffman.root)
        self.assertEqual(self.huffman.header, expected)

    def test_creating_header(self):
        expected = "0000000000110001000001110000010100000000001010000101010001001010001010101000001101000011000001010101010100001111111111110010010101010101"
        self.huffman.build_huffman_tree(self.text)
        self.huffman.create_bit_strings_dict()
        result = self.huffman.create_header(self.text)
        self.assertEqual(result, expected)

    def test_extract_data(self):
        compressed_data_str = "0000000000110001000001110000010100000000001010000101010001001010001010101000001101000011000001010101010100001111111111110010010101010101"
        header_data = "0001010000101010001001010001010101000001101000011"
        actual_data = "1010101010100001111111111110010010101010101"
        header_result, actual_data_result = self.huffman.parse_data(
            compressed_data_str)
        self.assertTupleEqual(
            (header_result, actual_data_result), (header_data, actual_data))

    def test_convert_header_data_to_bytes(self):
        expected = bytearray(b'\x001\x07\x05\x00(TJ*\x83C\x05U\x0f\xff%U')
        self.huffman.build_huffman_tree(self.text)
        self.huffman.create_bit_strings_dict()
        header_data = self.huffman.create_header(self.text)
        result = self.huffman.convert_header_data_to_bytes(header_data)
        self.assertEqual(result, expected)

    def test_rebuild_huffman_tree(self):
        expected_index = 49
        header_data = "0001010000101010001001010001010101000001101000011"
        root, index = self.huffman.rebuild_huffman_tree(header_data, 0)
        self.assertEqual(index, expected_index)

    def test_rebuild_huffman_tree_returns_None(self):
        header_data = "10000000"
        root, index = self.huffman.rebuild_huffman_tree(header_data, 9)
        self.assertFalse(root)

    def test_decode_text(self):
        expected = "AAAAAABCCCCCCDDEEEEE"
        compressed_data = "1010101010100001111111111110010010101010101"
        self.huffman.build_huffman_tree(self.text)
        huffman_codes = self.huffman.create_bit_strings_dict()
        result = self.huffman.decode_text(compressed_data, huffman_codes)
        self.assertEqual(result, expected)
