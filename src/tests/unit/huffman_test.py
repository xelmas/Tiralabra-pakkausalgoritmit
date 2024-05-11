import unittest
from algorithms.huffman import HuffmanCoding
import heapq


class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.text = "AAAAAABCCCCCCDDEEEEE"
        self.huffman = HuffmanCoding()
        self.min_bits = 8

    def test_creating_frequency_dict1(self):
        expected_result = {"A": 6, "B": 1, "C": 6, "D": 2, "E": 5, }
        result = self.huffman.create_frequency_dict(self.text)
        self.assertDictEqual(result, expected_result)

    def test_bit_string_defaults_to_zero(self):
        expected_result = {"A": "0"}
        huffman = HuffmanCoding()
        text = "A"
        huffman.create_frequency_dict(text)
        huffman.build_huffman_tree(text)
        result = huffman.create_bit_strings_dict()
        self.assertDictEqual(result, expected_result)

    def test_creating_min_heap(self):
        freq_dict = self.huffman.create_frequency_dict(self.text)
        min_heap = self.huffman.create_min_heap(freq_dict)
        lowest_prio_char = heapq.heappop(min_heap).char
        self.assertEqual(lowest_prio_char, "B")

    def test_merge_nodes(self):
        freq_dict = self.huffman.create_frequency_dict(self.text)
        min_heap = self.huffman.create_min_heap(freq_dict)
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

    def test_creating_complete_data(self):
        expected = "00110001000001110000010100000000001010000101010001001010001010101000001101000011000001010101010100001111111111110010010101010101"
        self.huffman.build_huffman_tree(self.text)
        self.huffman.create_bit_strings_dict()
        result = self.huffman.create_complete_data(self.text)
        self.assertEqual(result, expected)

    def test_extract_data(self):
        complete_compressed_data = "00110001000001110000010100000000001010000101010001001010001010101000001101000011000001010101010100001111111111110010010101010101"
        expected_header_data = "0001010000101010001001010001010101000001101000011"
        expected_actual_data = "1010101010100001111111111110010010101010101"
        self.huffman.min_bits = 8
        header_result, actual_data_result = self.huffman.parse_data(
            complete_compressed_data)
        print(header_result)
        print(actual_data_result)
        self.assertTupleEqual(
            (header_result, actual_data_result), (expected_header_data, expected_actual_data))

    def test_rebuild_huffman_tree(self):
        self.huffman.min_bits_char = 8
        self.huffman.min_bits = 8
        expected_index = 49
        header_data = "0001010000101010001001010001010101000001101000011"
        root, index = self.huffman.rebuild_huffman_tree(header_data, 0)
        self.assertEqual(index, expected_index)

    def test_rebuild_huffman_tree_returns_None_if_index_out_of_range(self):
        header_data = "10000000"
        root, index = self.huffman.rebuild_huffman_tree(header_data, 9)
        self.assertFalse(root)

    def test_decode_text(self):
        expected = self.text
        compressed_data = "1010101010100001111111111110010010101010101"
        self.huffman.build_huffman_tree(self.text)
        self.huffman.create_bit_strings_dict()
        huffman_codes = self.huffman.reverse_bit_strings
        result = self.huffman.decode_text(compressed_data, huffman_codes)
        self.assertEqual(result, expected)

    def test_compress(self):
        expected_result = "00110001000001110000010100000000001010000101010001001010001010101000001101000011000001010101010100001111111111110010010101010101"
        result = self.huffman.compress(self.text)
        self.assertEqual(result, expected_result)

    def test_decompress(self):
        expected_result = self.text
        self.huffman.min_bits_char = 8
        self.huffman.min_bits = 8
        compressed_data = "00110001000001110000010100000000001010000101010001001010001010101000001101000011000001010101010100001111111111110010010101010101"
        result = self.huffman.decompress(compressed_data)
        self.assertEqual(result, expected_result)

    def test_len_header_after_compression(self):
        huffman = HuffmanCoding()
        huffman.compress(self.text)
        expected_result = 49
        result = len(huffman.header)
        self.assertEqual(result, expected_result)

    def test_len_header_after_multiple_compression(self):
        huffman = HuffmanCoding()
        huffman.compress(self.text)
        huffman.compress(self.text)
        huffman.compress(self.text)
        expected_result = 49
        result = len(huffman.header)
        self.assertEqual(result, expected_result)

    def test_set_min_bits(self):
        huffman = HuffmanCoding()
        huffman.set_min_bits_needed(8)
        self.assertEqual(huffman.min_bits, 8)
        self.assertEqual(huffman.get_min_bits_needed(), 8)

    def test_set_min_bits_char(self):
        huffman = HuffmanCoding()
        huffman.set_min_bits_char(8)
        self.assertEqual(huffman.min_bits_char, 8)
        self.assertEqual(huffman.get_min_bits_char(), 8)

    def test_round_min_bits_dividable_by_eight(self):
        value = 10
        expected_result = 16
        result = self.huffman._round_min_bits_dividable_by_eight(value)
        self.assertEqual(result, expected_result)

    def test_calculate_and_set_min_bits(self):
        huffman = HuffmanCoding()
        huffman.compress(self.text)
        huffman._calculate_and_set_min_bits()
        self.assertEqual(huffman.min_bits, 8)

    def test_text_is_same_after_compression_and_decompression(self):
        huffman = HuffmanCoding()
        text = "WYS*WYGWYS*WYSWYSG"
        compressed_text = huffman.compress(text)
        decompressed_text = huffman.decompress(compressed_text)
        self.assertEqual(decompressed_text, text)

    def test_text_is_same_after_compression_and_decompression2(self):
        huffman = HuffmanCoding()
        text = "TOBEORNOTTOBEORTOBEORNOT"
        compressed_text = huffman.compress(text)
        decompressed_text = huffman.decompress(compressed_text)
        self.assertEqual(decompressed_text, text)

    def test_text_is_same_after_compression_and_decompression_with_large_unicode_value(self):
        text = "𐀀"
        huffman = HuffmanCoding()
        compressed_text = huffman.compress(text)
        decompressed_text = huffman.decompress(compressed_text)
        self.assertEqual(decompressed_text, text)
