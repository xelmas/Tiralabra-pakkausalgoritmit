import hypothesis.strategies as st
from hypothesis import given, example
from collections import Counter
import heapq
import math
import unittest

from algorithms.huffman import HuffmanCoding, Node


class TestInvariantHuffmanCoding(unittest.TestCase):
    def setUp(self):
        pass

    def _compare_min_heaps(self, heap1, heap2):
        if len(heap1) != len(heap2):
            return False

        for node1, node2 in zip(heap1, heap2):
            if node1.char != node2.char:
                return False

        return True

    def _create_heap(self, frequency_dict):
        expected_heap = []
        heapq.heapify(expected_heap)
        for symbol in frequency_dict:
            node = Node(symbol, frequency_dict[symbol])
            heapq.heappush(expected_heap, node)

        return expected_heap

    def _calculate_min_bits_needed(self, max_value):
        min_bits_needed = math.ceil(math.log2(max_value + 1))
        if min_bits_needed % 8 != 0:
            min_bits_needed += (8 - min_bits_needed % 8)

        return min_bits_needed

    @given(st.text())
    @example("A")
    def test_create_frequency_dict_consistency(self, text):
        huffman = HuffmanCoding()
        expected_freq = Counter(text)
        result_frequencies = huffman.create_frequency_dict(text)
        assert result_frequencies == expected_freq

    @given(st.dictionaries(st.characters(), st.integers(min_value=1)))
    @example({"A": 1})
    def test_create_min_heap_consistency(self, frequency_dict):
        huffman = HuffmanCoding()
        expected_heap = self._create_heap(frequency_dict)
        result_heap = huffman.create_min_heap(frequency_dict)
        assert self._compare_min_heaps(result_heap, expected_heap)

    @given(st.dictionaries(st.characters(), st.integers(min_value=1), min_size=1))
    def test_merge_nodes_consistency(self, freq_dict):
        huffman = HuffmanCoding()
        heap = self._create_heap(freq_dict)
        root_before_merging = heap[0].freq
        root_after_merging = huffman.merge_nodes(heap).freq
        self.assertLessEqual(root_before_merging, root_after_merging)

    @given(st.text(alphabet=st.characters(blacklist_characters="\x00"), min_size=1))
    def test_compression_decompression_consistency(self, text):
        huffman = HuffmanCoding()
        compressed_text = huffman.compress(text)
        decompressed_text = huffman.decompress(compressed_text)
        assert decompressed_text == text

    @given(st.text(min_size=1))
    def test_len_header_consistency_multiple_compressions(self, text):
        huffman = HuffmanCoding()
        huffman.compress(text)
        header_after_first_compress = huffman.header
        huffman.compress(text)
        header_after_second_compress = huffman.header
        assert header_after_second_compress == header_after_first_compress

    @given(st.text(min_size=1))
    def test_calculate_min_bits_consistency(self, text):
        huffman = HuffmanCoding()
        huffman.compress(text)
        header_len = len(huffman.header)
        expected_min_bits_needed = self._calculate_min_bits_needed(header_len)
        result = huffman.min_bits
        assert result == expected_min_bits_needed

    @given(st.dictionaries(st.characters(), st.integers(min_value=1), min_size=1))
    def test_calculate_min_bits_char_consistency(self, frequency_dict):
        expected_largest_value = max(ord(key) for key in frequency_dict.keys())
        expected_min_bits_needed = self._calculate_min_bits_needed(
            expected_largest_value)

        huffman = HuffmanCoding()
        huffman._calculate_and_set_min_bits_for_char(frequency_dict)
        result_largest_value = huffman._find_largest_unicode_value(
            frequency_dict)

        assert huffman.min_bits_char == expected_min_bits_needed
        assert result_largest_value == expected_largest_value
