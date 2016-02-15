__author__ = 'Florian Kibler'

from Converter import Converter

"""
Ausfuehrung des Converters
"""
if __name__ == '__main__':
    test = Converter('csv.csv')
    test.lesen()
    test.createfile('newf')
    test.addfile('csv2.csv','newf')