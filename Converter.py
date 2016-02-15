__author__ = 'Florian Kibler'

import csv, sys


class Converter(object):

    def __init__(self, pfad):
        self.pfad = pfad


    def lesen(self):
        filename = self.pfad + '.csv'
        out = []
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f, self.sniffer(filename))
                try:
                    for row in reader:
                        print(row)
                        out.append(row)
                except csv.Error as e:
                    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
            return out
        except FileNotFoundError as er:
            return 'Datei existiert nicht!'

    def sniffer(self, filename):
        moegliche_Trennzeichen = [',', ';', '\t', ' ', '|', ':']
        try:
            dialect = csv.Sniffer().sniff(filename + '.csv', moegliche_Trennzeichen)
        except:
            dialect = None
        return dialect

    def createfile(self):
        input = open(self.pfad + '.csv', "r")
        reader = csv.reader(input)
        output = open(self.pfad + 'NEW.csv', "w")
        writer = csv.writer(output, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            writer.writerow(row)
        input.close()
        output.close()

    def addfile(self,filename):
        input = open(filename + '.csv', "r")
        reader = csv.reader(input)
        output = open(self.pfad + 'NEW.csv', "a+")
        writer = csv.writer(output, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            writer.writerow(row)
        input.close()
        output.close()



if __name__ == '__main__':
    test = Converter("csv")
    test.lesen()
    test.createfile()
    test.addfile('csv2')

