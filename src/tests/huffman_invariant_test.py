import hypothesis.strategies as st
from hypothesis import given, example
from collections import Counter
import heapq
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

    ascii_strings = st.text(alphabet=st.characters(
        min_codepoint=0, max_codepoint=255), min_size=1)

    @given(ascii_strings)
    def test_compression_decompression_consistency(self, text):
        huffman = HuffmanCoding()
        compressed_text = huffman.compress(text)
        decompressed_text = huffman.decompress(compressed_text)
        assert decompressed_text == text
