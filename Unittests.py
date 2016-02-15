__author__ = 'Florian Kibler'

import unittest
from Converter import Converter


class TestsKorrekteAusfuehrung(unittest.TestCase):

    def test_korrekteAusfuehrungeinFile(self):
        c = Converter('csv.csv')

    def test_MehrereFiles_gleicherDialekt(self):
        c1 = Converter('csv.csv')
        c2 = Converter('csv2.csv')

    def test_MehrereFiles_unterschiedlicherDialekt(self):
        pass;

class Filenichtkorrekt(unittest.TestCase):
    """
    def test_something(self):
        self.assertEqual(True, False)
    """

    def test_Dateinichtvorhanden(self):
        pass;

    def test_UngueltigerDateiinhalt(self):
        pass;

    def test_KeinDateiinhalt(self):
        pass;



if __name__ == '__main__':
    unittest.main()
