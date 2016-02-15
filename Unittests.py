__author__ = 'Florian Kibler'

import unittest
from Converter import Converter


class Testsallgemein(unittest.TestCase):

    def setUp(self):
        self.f1=Converter('csv')
        self.f2=Converter('csv2')

    def test_readonefile(self):
        self.f1.readCSV()

    def test_writeonefile(self):
        self.f1.writeinCSV()

    def test_writetwofiles


if __name__ == '__main__':
    unittest.main()
