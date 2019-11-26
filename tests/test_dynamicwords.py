import unittest

from others.dynamicwords import findmostsimilarword


class DynamicWords(unittest.TestCase):

    def test_dinamic_words(self):
        self.assertEqual('fish', findmostsimilarword('fosh', 'fish', 'fort'))
        self.assertEqual('fish', findmostsimilarword('hish', 'fish', 'vista'))
        self.assertEqual('clues', findmostsimilarword('clue', 'clues', 'blue'))


if __name__ == '__main__':
    unittest.main()
