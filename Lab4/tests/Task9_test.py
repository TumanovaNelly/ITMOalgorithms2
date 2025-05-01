import unittest
from Lab4.src.Task9 import compress_string


class TestCompressString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(compress_string(""), "")

    def test_single_char(self):
        self.assertEqual(compress_string("a"), "a")

    def test_no_repeats(self):
        self.assertEqual(compress_string("abcdefg"), "abcdefg")

    def test_simple_repeats(self):
        self.assertEqual(compress_string("aabbccdd"), "aabbccdd")
        self.assertEqual(compress_string("aaaaaaabbbbbbccccc"), "a*7+b*6+c*5")
        self.assertEqual(compress_string("abcabcabc"), "abc*3")
        self.assertEqual(compress_string("abcdabcdabcd"), "abcd*3")

    def test_complex_repeats(self):
        self.assertEqual(compress_string("abcabcabcdefdefdefq"), "abc*3+def*3+q")


    def test_long_string(self):
        long_string = "xyzxyzxyzxyz" * 100
        expected = "xyz*400"
        self.assertEqual(compress_string(long_string), expected)



if __name__ == "__main__":
    unittest.main()