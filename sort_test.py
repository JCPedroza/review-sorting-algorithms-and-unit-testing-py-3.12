import unittest
from sort_repo import algorithms


class TestSort(unittest.TestCase):
    def setUp(self):
        self.algorithms = algorithms

    def test_empty(self):
        for algorithm in self.algorithms:
            self.assertEqual(
                algorithm.sort([]),
                [],
                algorithm.name,
            )

    def test_singleton(self):
        for algorithm in self.algorithms:
            self.assertEqual(
                algorithm.sort([5]),
                [5],
                algorithm.name,
            )

    def test_ordered(self):
        for algorithm in self.algorithms:
            self.assertEqual(
                algorithm.sort([0, 1, 2, 3]),
                [0, 1, 2, 3],
                algorithm.name,
            )

    def test_reversed(self):
        for algorithm in self.algorithms:
            self.assertEqual(
                algorithm.sort([3, 2, 1, 0]),
                [0, 1, 2, 3],
                algorithm.name,
            )

    def test_duplicates(self):
        for algorithm in self.algorithms:
            self.assertEqual(
                algorithm.sort([9, 5, 9, 1, 0, 1]),
                [0, 1, 1, 5, 9, 9],
                algorithm.name,
            )

    def test_negatives_odd_len(self):
        for algorithm in self.algorithms:
            self.assertEqual(
                algorithm.sort([-3, 5, -9, 0, 2, 7, -3]),
                [-9, -3, -3, 0, 2, 5, 7],
                algorithm.name,
            )

    def test_negatives_even_len(self):
        for algorithm in self.algorithms:
            self.assertEqual(
                algorithm.sort([-3, 5, -9, 0, 2, 7, 1, -3]),
                [-9, -3, -3, 0, 1, 2, 5, 7],
                algorithm.name,
            )


if __name__ == "__main__":
    unittest.main()
