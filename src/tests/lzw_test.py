import unittest
from lzw import LZW


class TestLZW(unittest.TestCase):
    def setUp(self):
        self.text = "WYS*WYGWYS*WYSWYSG"
        self.lzw = LZW()

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
        expected_result = "0000001000000000000001010111000000000001011001000000000001010011000000000000101010000000000100000000000000000001000111000000000100000000000000000100000010000000000100000110000000000100000110000000000001000111"
        encoded_text = self.lzw.encode(self.text)
        result = self.lzw.create_header(encoded_text)
        self.assertEqual(result, expected_result)

    def test_parse_data(self):
        expected = "000000000001010111000000000001011001000000000001010011000000000000101010000000000100000000000000000001000111000000000100000000000000000100000010000000000100000110000000000100000110000000000001000111"
        header_data = "0000001000000000000001010111000000000001011001000000000001010011000000000000101010000000000100000000000000000001000111000000000100000000000000000100000010000000000100000110000000000100000110000000000001000111"
        result = self.lzw.parse_data(header_data)
        self.assertEqual(result, expected)

    def test_decode_data(self):
        data = "000000000001010111000000000001011001000000000001010011000000000000101010000000000100000000000000000001000111000000000100000000000000000100000010000000000100000110000000000100000110000000000001000111"
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
        expected_result = "0000001000000000000001010111000000000001011001000000000001010011000000000000101010000000000100000000000000000001000111000000000100000000000000000100000010000000000100000110000000000100000110000000000001000111"
        result = self.lzw.compress(self.text)
        self.assertEqual(result, expected_result)

    def test_decompress(self):
        self.lzw._init_table(compress=False)
        expected_result = self.text
        binary_data_array = "0000001000000000000001010111000000000001011001000000000001010011000000000000101010000000000100000000000000000001000111000000000100000000000000000100000010000000000100000110000000000100000110000000000001000111"
        result = self.lzw.decompress(binary_data_array)
        self.assertEqual(result, expected_result)
