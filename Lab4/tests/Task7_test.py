import unittest

from typing import Tuple

from Lab4.src.Task7 import longest_common_substring


class TestLongestCommonSubstring(unittest.TestCase):
    def test_standard_cases(self):
        self.assertEqual(longest_common_substring("abcdef", "zabcd"), (1, 4))
        self.assertEqual(longest_common_substring("abcde", "cdefg"), (0, 3))

    def test_no_common_substring(self):
        self.assertEqual(longest_common_substring("abc", "def"), (0, 0))
        self.assertEqual(longest_common_substring("aaaa", "bbbb"), (0, 0))

    def test_empty_strings(self):
        self.assertEqual(longest_common_substring("", ""), (0, 0))
        self.assertEqual(longest_common_substring("", "abc"), (0, 0))
        self.assertEqual(longest_common_substring("abc", ""), (0, 0))

    def test_single_char_strings(self):
        self.assertEqual(longest_common_substring("a", "a"), (0, 1))
        self.assertEqual(longest_common_substring("a", "b"), (0, 0))

    def test_large_strings(self):
        string1 = "a" * 1000 + "b" * 1000
        string2 = "b" * 1000 + "c" * 1000
        self.assertEqual(longest_common_substring(string1, string2), (0, 1000))

    def test_edge_cases(self):
        self.assertEqual(longest_common_substring("abcdef", "abcxyz"), (0, 3))
        self.assertEqual(longest_common_substring("xyzabc", "xyzabc"), (0, 6))


if __name__ == "__main__":
    unittest.main()