import unittest
from random import randint

from Lab3.src.QuickMax import quick_max


class TestQuickMax(unittest.TestCase):
    def test_random_cases(self):
        for _ in range(1000):
            n = randint(1, 100)
            lst = [randint(-1000, 1000) for _ in range(n)]

            k = randint(0, n - 1)

            sorted_lst = sorted(lst, reverse=True)
            expected_result = sorted_lst[k]

            result = quick_max(lst[:], k)

            self.assertEqual(result, expected_result)

    def test_single_element(self):
        lst = [42]
        k = 0
        expected_result = 42
        self.assertEqual(quick_max(lst[:], k), expected_result)

    def test_all_elements_equal(self):
        lst = [5, 5, 5, 5]
        k = 2
        expected_result = 5
        self.assertEqual(quick_max(lst[:], k), expected_result)

    def test_first_maximum(self):
        lst = [3, 1, 4, 1, 5, 9, 2, 6]
        k = 0
        expected_result = 9
        self.assertEqual(quick_max(lst[:], k), expected_result)

    def test_last_maximum(self):
        lst = [3, 1, 4, 1, 5, 9, 2, 6]
        k = len(lst) - 1
        expected_result = 1
        self.assertEqual(quick_max(lst[:], k), expected_result)


if __name__ == "__main__":
    unittest.main()
