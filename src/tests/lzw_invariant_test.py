import hypothesis.strategies as st
from hypothesis import given, example
import unittest
import math

from algorithms.lzw import LZW


class TestInvariantLZW(unittest.TestCase):
    def setUp(self):
        pass

    ascii_strings = st.text(alphabet=st.characters(
        min_codepoint=0, max_codepoint=255), min_size=1)

    @given(ascii_strings)
    def test_compression_decompression_consistency(self, text):
        lzw = LZW()
        compressed_text = lzw.compress(text)
        decompressed_text = lzw.decompress(compressed_text)
        assert decompressed_text == text

    @given(st.lists(st.characters(min_codepoint=256), min_size=1))
    def test_set_extra_supported_symbols(self, extra_symbols):
        lzw = LZW()
        lzw.set_extra_supported_symbols(extra_symbols)
        assert lzw.extra_supported_symbols == extra_symbols

    @given(st.dictionaries(st.characters(), st.integers(min_value=1), min_size=1))
    def test_max_bits_consistency(self, table):
        lzw = LZW()
        lzw.table = table
        max_value = max(table.values())
        expected_result = math.ceil(math.log2(max_value + 1))
        min_bits_result = lzw.calculate_min_bits_needed()
        lzw.set_min_bits_needed(min_bits_result)
        assert min_bits_result == expected_result
        assert lzw.min_bits == expected_result
