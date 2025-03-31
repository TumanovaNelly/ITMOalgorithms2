import unittest

from Lab3.src.Prima import get_mst_lens


class TestGetMstLens(unittest.TestCase):
    def test_single_point(self):
        points = [(0, 0)]
        expected_result = []
        self.assertEqual(get_mst_lens(points), expected_result)

    def test_all_points_same(self):
        points = [(1, 1), (1, 1), (1, 1)]
        expected_result = [0, 0]
        self.assertEqual(get_mst_lens(points), expected_result)

    def test_points_on_line(self):
        points = [(0, 0), (1, 1), (2, 2), (3, 3)]
        expected_result = [2, 2, 2]  # Длины рёбер в MST
        self.assertEqual(get_mst_lens(points), expected_result)


if __name__ == "__main__":
    unittest.main()
