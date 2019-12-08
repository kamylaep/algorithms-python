import unittest

from others.goodoldfibonacci import recursive, dynamic, lasttwo


class BinarySearchTest(unittest.TestCase):

    def test_recursive(self):
        self.assertEqual(0, recursive(0))
        self.assertEqual(1, recursive(1))
        self.assertEqual(1, recursive(2))
        self.assertEqual(2, recursive(3))
        self.assertEqual(3, recursive(4))
        self.assertEqual(5, recursive(5))
        self.assertEqual(8, recursive(6))
        self.assertEqual(13, recursive(7))
        self.assertEqual(21, recursive(8))
        self.assertEqual(34, recursive(9))
        self.assertEqual(55, recursive(10))
        self.assertEqual(610, recursive(15))
        self.assertEqual(987, recursive(16))
        self.assertEqual(75025, recursive(25))
        self.assertEqual(121393, recursive(26))

    def test_dynamic(self):
        self.assertEqual(0, dynamic(0))
        self.assertEqual(1, dynamic(1))
        self.assertEqual(1, dynamic(2))
        self.assertEqual(2, dynamic(3))
        self.assertEqual(3, dynamic(4))
        self.assertEqual(5, dynamic(5))
        self.assertEqual(8, dynamic(6))
        self.assertEqual(13, dynamic(7))
        self.assertEqual(21, dynamic(8))
        self.assertEqual(34, dynamic(9))
        self.assertEqual(55, dynamic(10))
        self.assertEqual(610, dynamic(15))
        self.assertEqual(987, dynamic(16))
        self.assertEqual(75025, dynamic(25))
        self.assertEqual(121393, dynamic(26))

    def test_lasttwo(self):
        self.assertEqual(0, lasttwo(0))
        self.assertEqual(1, lasttwo(1))
        self.assertEqual(1, lasttwo(2))
        self.assertEqual(2, lasttwo(3))
        self.assertEqual(3, lasttwo(4))
        self.assertEqual(5, lasttwo(5))
        self.assertEqual(8, lasttwo(6))
        self.assertEqual(13, lasttwo(7))
        self.assertEqual(21, lasttwo(8))
        self.assertEqual(34, lasttwo(9))
        self.assertEqual(55, lasttwo(10))
        self.assertEqual(610, lasttwo(15))
        self.assertEqual(987, lasttwo(16))
        self.assertEqual(75025, lasttwo(25))
        self.assertEqual(121393, lasttwo(26))


if __name__ == '__main__':
    unittest.main()
