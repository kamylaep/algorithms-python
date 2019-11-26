import unittest

from sort.coutingsort import countingsort


class CountingSortTest(unittest.TestCase):

    def test_counting_sort(self):
        self.assertEqual([2, 3, 5, 15, 15], countingsort([2, 15, 3, 5, 15]))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], countingsort([8, 5, 6, 1, 2, 7, 9, 3, 0, 4]))
        self.assertEqual([2, 3, 5, 10], countingsort([10, 5, 2, 3]))
        self.assertEqual([], countingsort([]))
        self.assertEqual([], countingsort())
        self.assertEqual(None, countingsort(None))
        self.assertEqual([5], countingsort([5]))
        self.assertEqual([1, 2, ], countingsort([1, 2]))
        self.assertEqual([1, 2], countingsort([2, 1]))
        self.assertEqual([1, 2, 3, 4, 10], countingsort([1, 3, 4, 2, 10]))
        self.assertEqual([1, 1], countingsort([1, 1]))
        self.assertEqual([362, 452, 800, 800, 950], countingsort([800, 950, 362, 452, 800]))
        self.assertEqual([10, 26, 30, 80, 100050], countingsort([100050, 30, 80, 10, 26]))


if __name__ == '__main__':
    unittest.main()
