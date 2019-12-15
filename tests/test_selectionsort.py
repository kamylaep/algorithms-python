import unittest

from sort.selectionsort import selectionsort


class SelectionSortTest(unittest.TestCase):

    def test_selection_sort(self):
        self.assertEqual([2, 3, 5, 15, 15], selectionsort([2, 15, 3, 5, 15]))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                         selectionsort([8, 5, 6, 1, 2, 7, 9, 3, 0, 4]))
        self.assertEqual([2, 3, 5, 10], selectionsort([10, 5, 2, 3]))
        self.assertEqual([], selectionsort([]))
        self.assertEqual([], selectionsort())
        self.assertEqual(None, selectionsort(None))
        self.assertEqual([5], selectionsort([5]))
        self.assertEqual([1, 2, ], selectionsort([1, 2]))
        self.assertEqual([1, 2], selectionsort([2, 1]))
        self.assertEqual([1, 2, 3, 4, 10], selectionsort([1, 3, 4, 2, 10]))
        self.assertEqual([1, 1], selectionsort([1, 1]))
        self.assertEqual([362, 452, 800, 800, 950],
                         selectionsort([800, 950, 362, 452, 800]))
        self.assertEqual([10, 26, 30, 80, 100050],
                         selectionsort([100050, 30, 80, 10, 26]))


if __name__ == '__main__':
    unittest.main()
