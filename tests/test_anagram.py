import unittest

from others.anagram import isanagram


class AnagramTest(unittest.TestCase):

    def test_is_anagram(self):
        self.assertEqual(True, isanagram('rat', 'tar'))
        self.assertEqual(True, isanagram('cider', 'cried'))
        self.assertEqual(True, isanagram('cider', 'CriEd'))
        self.assertEqual(True, isanagram('Dormitory', 'Dirty room'))
        self.assertEqual(False, isanagram('dog', 'cat'))
        self.assertEqual(False, isanagram('big dog', 'small dog'))


if __name__ == '__main__':
    unittest.main()
