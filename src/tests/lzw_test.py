import unittest
from algorithms.lzw import LZW
from utilities.utils import calculate_min_bits_needed


class TestLZW(unittest.TestCase):
    def setUp(self):
        self.text = "WYS*WYGWYS*WYSWYSG"
        self.lzw = LZW()
        self.lzw.set_extra_supported_symbols([])
        self.lzw.min_bits = 9

    def test_init_table_compress(self):
        expected_table = {chr(i): i for i in range(256)}
        self.lzw._init_table(compress=True)
        result_table = self.lzw.get_table()
        self.assertDictEqual(result_table, expected_table)

    def test_init_table_decompress(self):
        expected_table = {i: chr(i) for i in range(256)}
        self.lzw._init_table(compress=False)
        result_table = self.lzw.get_table()
        self.assertDictEqual(result_table, expected_table)

    def test_encode(self):
        self.lzw._init_table(compress=True)
        expected = [87, 89, 83, 42, 256, 71, 256, 258, 262, 262, 71]
        encoded_array = self.lzw.encode(self.text)
        self.assertListEqual(encoded_array, expected)

    def test_create_header(self):
        self.lzw._init_table(compress=True)
        expected_result = "0000010100000001010111001011001001010011000101010100000000001000111100000000100000010100000110100000110001000111"
        encoded_text = self.lzw.encode(self.text)
        result = self.lzw.create_header(encoded_text)
        self.assertEqual(result, expected_result)

    def test_parse_data(self):
        expected = "000000000001010111000000000001011001000000000001010011000000000000101010000000000100000111000000000001000111000000000100000111000000000100001001000000000100001101000000000100001101000000000001000111"
        header_data = "0000001000000000000001010111000000000001011001000000000001010011000000000000101010000000000100000111000000000001000111000000000100000111000000000100001001000000000100001101000000000100001101000000000001000111"
        result = self.lzw.parse_data(header_data)
        self.assertEqual(result, expected)

    def test_decode_data(self):
        data = "001010111001011001001010011000101010100000000001000111100000000100000010100000110100000110001000111"
        decoded_data = self.lzw.decode_data(data)
        expected_data = [87, 89, 83, 42, 256, 71, 256, 258, 262, 262, 71]
        self.assertListEqual(decoded_data, expected_data)

    def test_decode_text(self):
        self.lzw._init_table(compress=False)
        decoded_data = [87, 89, 83, 42, 256, 71, 256, 258, 262, 262, 71]
        expected_result = self.text
        result = self.lzw.decode_text(decoded_data)
        self.assertEqual(result, expected_result)

    def test_compress(self):
        expected_result = "0000010100000001010111001011001001010011000101010100000000001000111100000000100000010100000110100000110001000111"
        result = self.lzw.compress(self.text)
        self.assertEqual(result, expected_result)

    def test_decompress(self):
        self.lzw._init_table(compress=False)
        expected_result = self.text
        binary_data_array = "0000010100000001010111001011001001010011000101010100000000001000111100000000100000010100000110100000110001000111"
        result = self.lzw.decompress(binary_data_array)
        self.assertEqual(result, expected_result)

    def test_extra_symbols_added_compression_table(self):
        lzw = LZW()
        extra_symbols = ["™", "“"]
        expected_table = {i: chr(i) for i in range(256)}
        code = 256
        for symbol in extra_symbols:
            expected_table[symbol] = code
            code += 1

        lzw.set_extra_supported_symbols(extra_symbols)
        lzw._init_table(compress=True)

    def test_extra_symbols_added_decompression_table(self):
        lzw = LZW()
        extra_symbols = ["™", "“"]
        expected_table = {i: chr(i) for i in range(256)}
        code = 256
        for symbol in extra_symbols:
            expected_table[code] = symbol
            code += 1

        lzw.set_extra_supported_symbols(extra_symbols)
        lzw._init_table(compress=False)
        self.assertDictEqual(lzw.get_table(), expected_table)

    def test_min_bits_needed(self):
        lzw = LZW()
        lzw._init_table(compress=True)
        min_bits_needed = calculate_min_bits_needed(max(lzw.get_table().values()))
        self.assertEqual(min_bits_needed, 8)
