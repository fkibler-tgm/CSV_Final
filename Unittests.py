__author__ = 'Florian Kibler'

import unittest
from Converter import Converter


class Testsallgemein(unittest.TestCase):

    def setUp(self):
        self.f1=Converter('csv')

    def test_readfile(self):
        self.f1.lesen()

    def test_writefile(self):
        self.f1.createfile()

    def test_twofiles(self):
        self.f1.createfile()
        self.f1.addfile('csv2')

    def test_wrongfilename(self):
        f3=Converter('notfoundfile')

    def test_emptyfile(self):
        f3=Converter('emptyfile')



if __name__ == '__main__':
    unittest.main()
