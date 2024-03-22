import unittest
import huffman
import heapq


class TestHuffmanCoding(unittest.TestCase):
    def setUp(self):
        self.huffman = huffman.HuffmanCoding("src/tests/testfile.txt")
        self.text = self.huffman.read_file()
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
