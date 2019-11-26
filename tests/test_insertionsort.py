import unittest

from sort.insertionsort import insertionsort


class InsertionSortTest(unittest.TestCase):

    def test_insertion_sort(self):
        self.assertEqual([2, 3, 5, 15, 15], insertionsort([2, 15, 3, 5, 15]))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], insertionsort([8, 5, 6, 1, 2, 7, 9, 3, 0, 4]))
        self.assertEqual([2, 3, 5, 10], insertionsort([10, 5, 2, 3]))
        self.assertEqual([], insertionsort([]))
        self.assertEqual([], insertionsort())
        self.assertEqual(None, insertionsort(None))
        self.assertEqual([5], insertionsort([5]))
        self.assertEqual([1, 2, ], insertionsort([1, 2]))
        self.assertEqual([1, 2], insertionsort([2, 1]))
        self.assertEqual([1, 2, 3, 4, 10], insertionsort([1, 3, 4, 2, 10]))
        self.assertEqual([1, 1], insertionsort([1, 1]))
        self.assertEqual([362, 452, 800, 800, 950], insertionsort([800, 950, 362, 452, 800]))
        self.assertEqual([10, 26, 30, 80, 100050], insertionsort([100050, 30, 80, 10, 26]))


if __name__ == '__main__':
    unittest.main()
