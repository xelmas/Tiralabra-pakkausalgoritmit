import hypothesis.strategies as st
from hypothesis import given
import unittest
import math

from algorithms.lzw import LZW
from utilities.utils import calculate_min_bits_needed


class TestInvariantLZW(unittest.TestCase):
    def setUp(self):
        pass

    def _find_extra_symbols(self, text):
        extra_supported_symbols = []
        for char in text:
            unicode = ord(char)
            if unicode > 255 and char not in extra_supported_symbols:
                extra_supported_symbols.append(char)

        return extra_supported_symbols

    ascii_strings = st.text(alphabet=st.characters(
        min_codepoint=0, max_codepoint=255), min_size=1)

    @given(ascii_strings)
    def test_compression_decompression_consistency_without_extra_symbols(self, text):
        lzw = LZW()
        compressed_text = lzw.compress(text)
        decompressed_text = lzw.decompress(compressed_text)
        assert decompressed_text == text

    @given(st.text(min_size=1))
    def test_compression_decompression_consistency_with_extra_symbols(self, text):
        extra_supported_symbols = self._find_extra_symbols(text)
        lzw = LZW()
        lzw.set_extra_supported_symbols(extra_supported_symbols)
        compressed_text = lzw.compress(text)
        decompressed_text = lzw.decompress(compressed_text)
        assert decompressed_text == text

    @given(st.lists(st.characters(min_codepoint=256), min_size=1))
    def test_set_extra_supported_symbols(self, extra_symbols):
        lzw = LZW()
        lzw.set_extra_supported_symbols(extra_symbols)
        assert lzw.extra_supported_symbols == extra_symbols

    @given(st.dictionaries(st.characters(), st.integers(min_value=1), min_size=1))
    def test_min_bits_consistency(self, table):
        lzw = LZW()
        lzw.table = table
        max_value = max(table.values())
        expected_result = math.ceil(math.log2(max_value + 1))
        min_bits_result = calculate_min_bits_needed(max_value)
        lzw.set_min_bits_needed(min_bits_result)
        assert min_bits_result == expected_result
        assert lzw.min_bits == expected_result
