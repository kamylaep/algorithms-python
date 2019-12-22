import unittest

from others.countingstrings import count


class CountingStrings(unittest.TestCase):

    def test_counting_strings(self):
        self.assertEqual(1000000000000, count('a', 'a', 1000000000000))
        self.assertEqual(3, count('ababahgeytuca', 'a', 5))
        self.assertEqual(3, count('ababa', 'a', 5))
        self.assertEqual(7, count('aba', 'a', 10))
        self.assertEqual(203302892858, count('beeaabc', 'a', 711560125001))
        self.assertEqual(51574523448, count(
            'kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm', 'a', 736778906400))


if __name__ == '__main__':
    unittest.main()
