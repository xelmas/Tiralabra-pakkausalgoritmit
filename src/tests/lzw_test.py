import unittest
from lzw import LZW


class TestLZW(unittest.TestCase):
    def setUp(self):
        self.lzw = LZW("src/tests/testfile2.txt")
        self.text = self.lzw.file_handler.read_file()

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

    def test_convert_data_to_bytes(self):
        self.lzw._init_table(compress=True)
        expected_result = bytearray(
            b'\x04\x00W\x05\x90S\x02\xa1\x00\x04q\x00\x10!\x06\x10`G')
        encoded_array = self.lzw.encode(self.text)
        header_str = self.lzw.create_header(encoded_array)
        header_bin = self.lzw.convert_data_to_bytes(header_str)
        self.assertEqual(header_bin, expected_result)

    def test_parse_data(self):
        expected = "000001010111000001011001000001010011000000101010000100000000000001000111000100000000000100000010000100000110000100000110000001000111"
        header_data = "000001000000000001010111000001011001000001010011000000101010000100000000000001000111000100000000000100000010000100000110000100000110000001000111"
        result = self.lzw.parse_data(header_data)
        self.assertEqual(result, expected)

    def test_decode_text(self):
        data = "000001010111000001011001000001010011000000101010000100000000000001000111000100000000000100000010000100000110000100000110000001000111"
        decoded_data = self.lzw.decode_text(data)
        print(decoded_data)
        expected_data = [87, 89, 83, 42, 256, 71, 256, 258, 262, 262, 71]
        self.assertListEqual(decoded_data, expected_data)

    def test_decode(self):
        self.lzw._init_table(compress=False)
        decoded_data = [87, 89, 83, 42, 256, 71, 256, 258, 262, 262, 71]
        expected_result = "WYS*WYGWYS*WYSWYSG"
        result = self.lzw.decode(decoded_data)
        self.assertEqual(result, expected_result)
