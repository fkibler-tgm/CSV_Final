__author__ = 'Florian Kibler'

import unittest
from Converter import Converter


class TestsKorrekteAusfuehrung(unittest.TestCase):

    def setUp(self):
        self.f1=Converter('csv')
        self.f2=Converter('csv2')

    def test_korrekteAusfuehrungeinFile(self):
        pass;

    def test_MehrereFiles_gleicherDialekt(self):
        pass;

    def test_MehrereFiles_unterschiedlicherDialekt(self):
        pass;

    def test_Dateinichtvorhanden(self):
        pass;

    def test_UngueltigerDateiinhalt(self):
        pass;



if __name__ == '__main__':
    unittest.main()
