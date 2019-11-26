import unittest

from search.binarysearch import binarysearch


class BinarySearchTest(unittest.TestCase):


    def test_binary_search(self):
        elements = range(10)
        self.assertEqual(5, binarysearch(5, elements))
        self.assertEqual(9, binarysearch(9, elements))
        self.assertEqual(-1, binarysearch(10, elements))
        self.assertEqual(0, binarysearch(0, elements))
        self.assertEqual(2, binarysearch(2, elements))
        self.assertEqual(-1, binarysearch(2))
        self.assertEqual(-1, binarysearch(2, None))


if __name__ == '__main__':
    unittest.main()
