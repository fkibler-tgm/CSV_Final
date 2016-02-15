__author__ = 'Florian Kibler'

import csv, sys

"""
Jene Klasse nimmt ein csv-File entgegen. Hierbei ist es dann mit den sich in der Klasse befindlichen Methoden moeglich
den Inhalt in ein anderes File zu schreiben. Zudem ist es moeglich ein weiteres File dazu zu addieren, welches dann
in dem neuen File angehaengt wird.
"""


class Converter(object):
    def __init__(self, path):
        self.path = path

    def lesen(self):
        """
        Mittels dieser Methode kann eine CSV-Datei auf der Konsole ausgelesen werden. Falls
        es zu Problemen kommt (falsche File-Bezeichnung -> File wird nicht gefunden), wird
        der String Datei existiert nicht! geschreiben.
        :return: INhalt des CSV-Files
        """
        filename = self.path
        content = []
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f, self.sniffer(filename))
                try:
                    for row in reader:
                        print(row)
                        content.append(row)
                except csv.Error as e:
                    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
            return content
        except FileNotFoundError as er:
            print('Datei existiert nicht!')
            return ' ';

    def sniffer(self, filename):
        """
        Nimmt eine Datei entgegen und erkennt mittels dem CSV-sniffer, welcher dialekt verwendet wird.
        :param: Name des CSV-Files
        :return: Dialektname
        """
        pdialect = [',', ';', '\t', ' ', '|', ':']
        try:
            dialect = csv.Sniffer().sniff(filename + '.csv', pdialect)
        except:
            dialect = None
        return dialect

    def createfile(self,newfilename):
        """
        Erstellt eine neues File mit dem Inhalt von der CSV-Datei
        :param: Name des Neuen Files
        """
        input = open(self.path, "r")#das File mit dem Inhalt wird geoeffnet r-> read-Rechte
        reader = csv.reader(input)
        output = open(newfilename, "w")#das neue File wird geoeffnet, bzw. erstellt w-> write-Rechte
        writer = csv.writer(output, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            writer.writerow(row) #schreibt in das neue File rein
        input.close()
        output.close()

    def addfile(self, filename,newfilename):
        """
        Kann zu dem bestehenden File dazuschreiben
        :param filename: Nimmt Namen des Files entgegen, wessen inhalt gilt zu dem gewuenschten file hinzuzufuegen
        :param newfilename: Nimmt Namen des Files etngegen, zu welchem der COntent hinzugefuegt werden soll
        """
        input = open(filename, "r")
        reader = csv.reader(input)
        output = open(newfilename, "a+")#a# bedeutet nicht ueberschreiben, sondern dazuschreiben
        writer = csv.writer(output, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in reader:
            writer.writerow(row)
        input.close()
        output.close()


"""
if __name__ == '__main__':
    test = Converter('csv.csv')
    test.lesen()
    test.createfile('newf')
    test.addfile('csv2.csv','newf')
"""

