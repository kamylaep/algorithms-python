import unittest

from sort.bubblesort import bubblesort


class BubbleSortTest(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], bubblesort([8, 5, 6, 1, 2, 7, 9, 3, 0, 4]))
        self.assertEqual([2, 3, 5, 10], bubblesort([10, 5, 2, 3]))
        self.assertEqual([], bubblesort([]))
        self.assertEqual([], bubblesort())
        self.assertEqual(None, bubblesort(None))
        self.assertEqual([5], bubblesort([5]))
        self.assertEqual([1, 2, ], bubblesort([1, 2]))
        self.assertEqual([1, 2], bubblesort([2, 1]))
        self.assertEqual([1, 2, 3, 4, 10], bubblesort([1, 3, 4, 2, 10]))
        self.assertEqual([1, 1], bubblesort([1, 1]))


if __name__ == '__main__':
    unittest.main()
