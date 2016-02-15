__author__ = 'Florian Kibler'

import unittest
from Converter import Converter


class Testsallgemein(unittest.TestCase):

    def setUp(self):
        self.f1=Converter('csv')
        self.f2=Converter('csv2')

    def test_readfile(self):
        self.f1.lesen()

    def test_writefile(self):
        self.f1.schreiben()

    def test_wrongfilename(self):
        f3=Converter('notfoundfile')

    def test_emptyfile(self):
        f3=Converter('emptyfile')



if __name__ == '__main__':
    unittest.main()
