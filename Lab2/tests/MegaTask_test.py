import unittest
from random import randint, choice

from Lab2.src.Rope import Rope


class TestRope(unittest.TestCase):
    def setUp(self):
        self.string = Rope()

    def test_random_operations(self):
        word = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for _ in range(randint(1, 100)))
        self.string.build(word)

        for _ in range(100):
            from_start = randint(0, len(word) - 1)
            from_end = randint(from_start, len(word) - 1)
            to_index = randint(0, len(word) - (from_end - from_start + 1))

            self.string.cut_n_paste((from_start, from_end), to_index)

            substring = word[from_start:from_end + 1]
            word = word[:from_start] + word[from_end + 1:]
            word = word[:to_index] + substring + word[to_index:]

            self.assertEqual(str(self.string), word)

    def test_paste_to_start(self):
        self.string.build("abcde")
        self.string.cut_n_paste((1, 3), 0)
        self.assertEqual(str(self.string), "bcdae")

    def test_getitem(self):
        self.string.build("abcde")
        self.assertEqual(self.string[0], 'a')
        self.assertEqual(self.string[0], 'a')
        self.assertEqual(self.string[4], 'e')
        self.string.cut_n_paste((1, 3), 0)
        self.assertEqual(self.string[0], 'b')
        self.assertEqual(self.string[0], 'b')
        self.assertEqual(self.string[4], 'e')

    def test_paste_to_end(self):
        self.string.build("abcde")
        self.string.cut_n_paste((1, 3), 2)
        self.assertEqual(str(self.string), "aebcd")

    def test_cut_all_word(self):
        self.string.build("abcde")
        self.string.cut_n_paste((0, 4), 0)
        self.assertEqual(str(self.string), "abcde")
        self.assertRaises(IndexError, self.string.cut_n_paste, (0, 4), 1)

    def test_index_error(self):
        self.string.build("abcde")
        self.assertRaises(IndexError, self.string.cut_n_paste, (1, 2), 4)
        self.assertRaises(IndexError, self.string.cut_n_paste, (1, 2), -1)
        self.assertRaises(IndexError, self.string.cut_n_paste, (-1, 2), 1)
        self.assertRaises(IndexError, self.string.cut_n_paste, (1, -2), 1)
        self.assertRaises(IndexError, self.string.cut_n_paste, (2, 1), 1)


if __name__ == "__main__":
    unittest.main()
